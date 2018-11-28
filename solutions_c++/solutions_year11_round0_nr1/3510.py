#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, char> Task;
typedef vector<Task> Tasks;

size_t FindTask(size_t from, char robot, const Tasks& tasks)
{
	while (from < tasks.size() && tasks[from].second != robot)
		++from;
	return from;
}

int sign(int n)
{
	if (n < 0)
		return -1;
	else if (n > 0)
		return 1;
	else
		return 0;
}

int main()
{
	int numTests = 0;
	string numTestsStr;
	getline(cin, numTestsStr);
	stringstream ssTests(numTestsStr);
	ssTests >> numTests;
	for (int test = 1; test <= numTests; ++test)
	{
		string s;
		getline(cin, s);

		stringstream ss(s);
		int numTasks = 0;
		ss >> numTasks;

		Tasks tasks;
		while (numTasks --> 0)
		{
			int b = 0;
			char r = '\0';
			ss >> r >> b;

			tasks.push_back(Task(b, r));
		}

		int answer = 0;
		int orangePos = 1, bluePos = 1;
		size_t nextOrangeTask = FindTask(0, 'O', tasks), nextBlueTask = FindTask(0, 'B', tasks);
		while (nextOrangeTask < tasks.size() || nextBlueTask < tasks.size())
		{
			++answer;
			if (nextOrangeTask < nextBlueTask)
			{
				if (orangePos == tasks[nextOrangeTask].first)
					nextOrangeTask = FindTask(nextOrangeTask + 1, 'O', tasks);
				else
					orangePos += sign(tasks[nextOrangeTask].first - orangePos);

				if (nextBlueTask < tasks.size())
					bluePos += sign(tasks[nextBlueTask].first - bluePos);
			}
			else
			{
				if (bluePos == tasks[nextBlueTask].first)
					nextBlueTask = FindTask(nextBlueTask + 1, 'B', tasks);
				else
					bluePos += sign(tasks[nextBlueTask].first - bluePos);

				if (nextOrangeTask < tasks.size())
					orangePos += sign(tasks[nextOrangeTask].first - orangePos);
			}
		}

		cout << "Case #" << test << ": " << answer << endl;
	}

	return 0;
}
