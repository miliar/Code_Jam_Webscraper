#include <stdio.h>
#include <vector>

using namespace std;

typedef int ButtonId;
enum Robot
{
	ORANGE,
	BLUE
};

Robot
read_robot_type()
{ /* {{{ */
	while (1)
	{
		int r = getchar();
		switch (r)
		{
			case 'O':
				return Robot::ORANGE;
			case 'B':
				return Robot::BLUE;
			// default continuing loops
		}
	}
} /* }}} */

ButtonId
read_button_id()
{ /* {{{ */
	int hoge;
	scanf("%d", &hoge);
	return hoge;
} /* }}} */

typedef std::vector<std::pair<Robot, ButtonId>> TestCase;

ButtonId
get_next_button(Robot r, TestCase::iterator iter, TestCase::iterator end)
{
	for (; iter != end; ++iter)
	{
		if ((*iter).first == r) //robot for whom we are searching
			return (*iter).second;
	}
	return -1; //not found
}

// returns a resulting time for the given input.
int
solve(int i, TestCase input)
{
	int time = 0;

	ButtonId curr_o = 1; //position of robot O of the time.
	ButtonId curr_b = 1; //same for B

	auto task = input.begin();

	while (1)
	{
		Robot task_robot = (*task).first;
		ButtonId task_button = (*task).second;

		ButtonId next_o = get_next_button(Robot::ORANGE, task, input.end());
		ButtonId next_b = get_next_button(Robot::BLUE, task, input.end());

		// if no more tasks for both robots, then finish
		if (next_o == -1 && next_b == -1)
			return time;

		// for orange robot
		if (-1 == next_o)
		{
			// no more tasks for robot o
		}
		else if (curr_o == next_o)
		{
			//if current task is to press button next_o for orange.
			if (task_robot == Robot::ORANGE
					&& task_button == curr_o)
			{
				++task; //next task
			}
			else {
			//stay there
			}
		}
		else if (curr_o > next_o)
		{
			//move backward
			--curr_o;
		}
		else if (curr_o < next_o)
		{
			//move forward
			++curr_o;
		}

		//for blue robot
		if (curr_b == next_b)
		{
			if (task_robot == Robot::BLUE
					&& task_button == curr_b)
			{
				++task;
			}
			else {
			//else stay there
			}
		}
		else if (curr_b > next_b)
		{
			//move back
			--curr_b;
		}
		else if (curr_b < next_b)
		{
			//move forward
			++curr_b;
		}

		++time;
	}
}

void
exec_test(int test_id)
{
	std::vector<std::pair<Robot, ButtonId>> input;

	int length = 0;
	scanf("%d", &length);
	for (int i = 0; i < length; ++i)
	{
		Robot a = read_robot_type();
		ButtonId b = read_button_id();
		input.push_back(make_pair(a, b));
	}

	//for (auto iter = input.begin(); iter != input.end(); ++iter)
	//{
	//	Robot a = (*iter).first;
	//	ButtonId b = (*iter).second;
	//}
	//
	int result = solve(test_id, input);

	printf("Case #%d: %d\n", test_id+ 1, result);
}

int
main(int argc, char const **argv)
{
	int n_tests = 0;
	scanf("%d", &n_tests);

	for (int i = 0; i < n_tests; ++i)
		exec_test(i);
	
	return 0;
}
