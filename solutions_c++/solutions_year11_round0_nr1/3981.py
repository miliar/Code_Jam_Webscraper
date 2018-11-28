// BotTrust.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

enum Robot {
	Orange = 0, 
	Blue
};

struct Task {
	int button;
	Robot robot;
	Task() : button(0), robot(Orange) {}
	Task(int _button, Robot _robot) : button(_button), robot(_robot) { }
};

int perfomTasks(const vector<Task>& tasks)
{
	int numSteps = 0;
	int pos[2] = { 1, 1 };
	for (vector<Task>::const_iterator i = tasks.begin(); i != tasks.end(); ++i)
	{
		int mainSteps = abs(i->button - pos[i->robot]) + 1;
		pos[i->robot] = i->button;
		for (vector<Task>::const_iterator j = i + 1; j != tasks.end(); ++j)
			if (j->robot != i->robot) {
				int secSteps = abs(j->button - pos[j->robot]);
				if (secSteps > mainSteps)
					secSteps = mainSteps;
				pos[j->robot] += (j->button - pos[j->robot] > 0) ? secSteps : -secSteps;
				break;
			}
		numSteps += mainSteps;
	}
	return numSteps;
}

int main(int argc, char* argv[])
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		vector<Task> tasks;
		int numTasks = 0;
		cin >> numTasks;
		for (int j = 0; j < numTasks; j++) {
			Task task;
			char crobot = '\0';
			cin >> crobot;
			task.robot = crobot == 'O' ? Orange : Blue;
			cin >> task.button;
			tasks.push_back(task);
		}

		int steps = perfomTasks(tasks);
		cout << "Case #" << i+1 << ": " << steps << endl;
	}

	return 0;
}

