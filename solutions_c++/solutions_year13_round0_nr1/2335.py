
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <Windows.h>
#include <algorithm>

using namespace std;

CRITICAL_SECTION		CS;

enum TASK_STATE
{
	TASK_ADDED,
	TASK_PROCESSING,
	TASK_COMPLETED,
};

struct task
{
	int						case_number;
	int						state;
	string					result;

	char					desk[16];

	task					(int case_number) : case_number(case_number), state(TASK_ADDED) {}
};

struct task_pred {
  bool		operator()		(const task& lhs, const task& rhs) {
	  return lhs.case_number < rhs.case_number;
  }
};

vector<task>				tasks;

bool diagonal				(task& t, char v)
{
	bool won				= true;
	for (int i=0; i<4; ++i) {
		char c				= t.desk[i*4+i];
		if (c != v && c != 'T') {
			won				= false;
			break;
		}
	}
	if (won)				return true;
	
	won					= true;
	for (int i=0; i<4; ++i) {
		char c				= t.desk[i*4+(3-i)];
		if (c != v && c != 'T') {
			won				= false;
			break;
		}
	}
	if (won)				return true;
	return false;
}

bool col_or_row				(task& t, char v)
{
	for (int i=0; i<4; ++i) {
		bool won			= true;
		for (int j=0; j<4; ++j) {
			char c			= t.desk[i*4+j];
			if (c != v && c != 'T') {
				won			= false;
				break;
			}
		}
		if (won)			return true;
		won					= true;
		for (int j=0; j<4; ++j) {
			char c			= t.desk[j*4+i];
			if (c != v && c != 'T') {
				won			= false;
				break;
			}
		}
		if (won)			return true;
	}
	return false;
}

void execute_task			(task& t)
{
	if (diagonal(t, 'X')) {
		t.result			= "X won";
		return;
	}
	if (diagonal(t, 'O')) {
		t.result			= "O won";
		return;
	}
	if (col_or_row(t, 'X')) {
		t.result			= "X won";
		return;
	}
	if (col_or_row(t, 'O')) {
		t.result			= "O won";
		return;
	}
	for (int i=0; i<16; ++i) {
		if (t.desk[i] == '.') {
			t.result		= "Game has not completed";
			return;
		}
	}
	t.result				= "Draw";
}

bool get_line				(ifstream& stream, char* buffer, int buffer_size)
{
	if (!stream.good()) {
		cout << "wrong input file format" << endl;
		return false;
	}
	stream.getline			(buffer, buffer_size);
	return true;
}

bool read_task				(task& t, ifstream& file)
{
	char buffer[4*4096];
	for (int i=0; i<4; ++i) {
		if (!get_line(file, buffer, sizeof(buffer))) {
			return false;
		}
		for (int j=0; j<4; ++j) {
			t.desk[i*4+j] = buffer[j];
		}
	}
	get_line				(file, buffer, sizeof(buffer));
	return true;
}

void print_task				(task& t)
{
	cout << "Task #" << t.case_number << " Text = " << t.desk << endl;
}

void print_result			(task& t)
{
	cout << "Case #" << t.case_number << ": " << t.result.c_str() << endl;
}

DWORD WINAPI worker_thread	(void* arg)
{
	while (true) {
		task* t				= 0;
		{
			EnterCriticalSection(&CS);
			for (int i=0, size=tasks.size(); i!=size; ++i) {
				if (tasks[i].state == 0) {
					t		= &tasks[i];
					t->state= TASK_PROCESSING;
					break;
				}
			}
			LeaveCriticalSection(&CS);
		}
		if (t == 0) {
			return 0;
		}
		execute_task		(*t);
		t->state			= TASK_COMPLETED;
	}
	return 0;
}

int main					(int argc, char** argv)
{
	if (argc < 2) {
		cout << "Input file missing" << endl;
		return -1;
	}
	int time				= timeGetTime();
	ifstream file			(argv[1]);
	if (!file.is_open()) {
		return -1;
	}
	char line[4*4096];
	file.getline			(line, sizeof(line));
	int line_count			= atoi(line);
	for (int i=0; i!=line_count; ++i) {
		task t(i+1);
		if (!read_task(t, file)) {
			return -1;
		}
		tasks.push_back		(t);
	}

	if (IsDebuggerPresent()) {
		for (int i=0; i!=tasks.size(); ++i) {
			task& t			= tasks[i];
			//print_task	(t);
			execute_task	(t);
			print_result	(t);
		}
	} else {
		InitializeCriticalSection(&CS);
		HANDLE handles[4];
		for (int i=0; i<4; ++i) {
			handles[i]			= CreateThread( NULL, 0, &worker_thread, 0, 0, 0);
		}
		WaitForSingleObject		(handles[0], INFINITE);
		WaitForSingleObject		(handles[1], INFINITE);
		WaitForSingleObject		(handles[2], INFINITE);
		WaitForSingleObject		(handles[3], INFINITE);
		DeleteCriticalSection	(&CS);
		::sort					(tasks.begin(), tasks.end(), task_pred());
		//cout << "Work done in [" << timeGetTime() - time << "] ms" << endl;
		for (int i=0; i!=tasks.size(); ++i) {
			print_result		(tasks[i]);
		}
	}
	return 0;
}
