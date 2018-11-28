
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

	int						surprising_triplets;
	int						max_score;
	vector<int>				points;

	task					(int case_number) : case_number(case_number), state(TASK_ADDED) {}
};

struct task_pred {
  bool		operator()		(const task& lhs, const task& rhs) {
	  return lhs.case_number < rhs.case_number;
  }
};

vector<task>				tasks;

bool get_line				(ifstream& stream, char* buffer, int buffer_size)
{
	if (!stream.good()) {
		cout << "wrong input file format" << endl;
		return false;
	}
	stream.getline			(buffer, buffer_size);
	return true;
}

int get_result				(task& t)
{
	int result				= 0;
	int odd					= t.surprising_triplets;
	for (unsigned int i=0; i<t.points.size(); ++i) {
		int score			= t.points[i];
		int base			= score / 3;
		int rest			= score % 3;
		if (base >= t.max_score) {
			++result;
			continue;
		}
		if (rest && base+1==t.max_score) {
			++result;
			continue;
		}
		if (odd && base > 0) {
			switch (rest) {
			case 0:
				{
					// score == 3 * n = {n-1, n, n+1}
					if (base + 1 == t.max_score) {
						--odd;
						++result;
						continue;
					}
				} break;
			case 1:
				{
					// score == 3 * n + 1 = {n, n, n+1}
				} break;
			case 2:
				{
					// score == 3 * n + 2 = {n, n, n+2}
					if (base + 2 == t.max_score) {
						--odd;
						++result;
						continue;
					}
				} break;
			}
		}
	}
	return result;
}

void execute_task			(task& t)
{
	int result				= get_result(t);
	char buf[80];
	sprintf_s				(buf, "%d", result);
	t.result				= buf;
}

bool read_task				(task& t, ifstream& file)
{
	char line[4*4096];
	if (!get_line(file, line, sizeof(line))) {
		return false;
	}
	stringstream ss			(line);
	int count;
	ss >> count;
	ss >> t.surprising_triplets;
	ss >> t.max_score;
	for (int i=0; i<count; ++i) {
		int point;
		ss >> point;
		t.points.push_back	(point);
	}
	return true;
}

void print_task				(task& t)
{
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

	if (1 || IsDebuggerPresent()) {
		for (int i=0; i!=tasks.size(); ++i) {
			task& t			= tasks[i];
			execute_task	(t);
			//print_task		(t);
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
