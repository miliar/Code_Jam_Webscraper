// bottrust.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <list>
using namespace std;

typedef enum {BLUE, ORANGE} robot;
typedef enum {FORWARD, BACKWARD, STAY, PUSH} robot_action;
typedef struct
{
	robot r;
	int b; // button
} goal;

goal make_goal(char rb, int rb_num)
{
	goal g;
	if (rb == 'O')
		g.r = ORANGE;
	else
		g.r = BLUE;
	g.b = rb_num;
	return g;
}

robot_action determine_robot_action(int pos, goal current_team_goal, goal current_robot_goal)
{
	// first, let's deal with whether we can push the button:
	if ((current_team_goal.r == current_robot_goal.r) && (pos == current_robot_goal.b))
	{
		return PUSH;
	}
	// if not, then we need to move
	if (pos == current_robot_goal.b)
	{
		return STAY;
	} else if (pos < current_robot_goal.b)
	{
		return FORWARD;
	} else 
	{
		return BACKWARD;
	}
}

int main(int argc, char* argv[])
{
	int num_tests = -1;
	int num_goals;
	list<goal> team_goals;
	list<goal> orange_goals;
	list<goal> blue_goals;
	goal new_goal;

	char rb[20];
	int rb_num;

	printf("Running\n");

	FILE * fin = fopen(argv[1], "r");
	if (!fin)
	{
		printf("Couldn't open input file\n");
		return 1;
	}
	FILE * fout = fopen(argv[2], "w");
	if (!fout)
	{
		printf("Couldn't open output file\n");
		return 2;
	}

	fscanf(fin,"%d",&num_tests);
	printf("Number of tests = %d\n", num_tests);

	// read in the data and process for each goal
	for (int i = 0; i < num_tests; i++)
	{
		team_goals.clear();
		orange_goals.clear();
		blue_goals.clear();

		fscanf(fin,"%d",&num_goals);
		printf("Number of goals = %d\n",num_goals);
		
		for (int j = 0; j < num_goals; j++)
		{
			fscanf(fin, "%s %d", rb, &rb_num);
			new_goal = make_goal(rb[0], rb_num);
			team_goals.push_back(new_goal);
			if (new_goal.r == ORANGE)
				orange_goals.push_back(new_goal);
			else
				blue_goals.push_back(new_goal);
			printf("Goal %d: %c %d\n", j, (new_goal.r == ORANGE) ? 'O' : 'B', new_goal.b);
		}

		printf("Goal list length = %d, orange list = %d, blue list = %d\n", team_goals.size(), orange_goals.size(), blue_goals.size());

		// now let's play the game
		int orange_position = 1;
		int blue_position = 1;
		int num_iters = 0;
		robot_action orange_action = STAY;
		robot_action blue_action = STAY;
		
		while (!team_goals.empty())
		{
			num_iters ++;
			if (orange_goals.empty())
				orange_action = STAY;
			else
				orange_action = determine_robot_action(orange_position, team_goals.front(), orange_goals.front());
			
			if (blue_goals.empty())
				blue_action = STAY;
			else
				blue_action = determine_robot_action(blue_position, team_goals.front(), blue_goals.front());
			
			if (orange_action == PUSH && blue_action == PUSH)
				return 42;
			
			switch (orange_action)
			{
			case PUSH:
				team_goals.pop_front();
				orange_goals.pop_front();
				break;
			case FORWARD:
				orange_position ++;
				break;
			case BACKWARD:
				orange_position --;
				break;
			case STAY:
				break;
			}
			switch (blue_action)
			{
			case PUSH:
				team_goals.pop_front();
				blue_goals.pop_front();
				break;
			case FORWARD:
				blue_position ++;
				break;
			case BACKWARD:
				blue_position --;
				break;
			case STAY:
				break;
			}
			printf("Iter %d: O %d %d\tB %d %d\n", num_iters, orange_action == PUSH, orange_position, blue_action == PUSH, blue_position);

		}

		fprintf(fout, "Case #%d: %d\n", i+1, num_iters);
	}

	fclose(fout);
	fclose(fin);

    return 0;
}