// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <iostream>

using std::cin;
using std::cout;

struct Action
{
	int			Robot;
	int			Button;
};

struct Robot
{
	int			Id;
	int			Location;

	explicit Robot(int id) : Id(id), Location(1) {}

	// Returns true if we had to move in some direction, false if we're already at the location
	bool MoveTo(int location)
	{
		if( Location == location )
			return false;

		if( Location < location )
			++Location;
		else
			--Location;

		return true;
	}
};

bool UpdateRobots( Robot & a, Robot & b, size_t active_action, const std::vector<Action> & actions )
{
	bool press_button = false;

	if( !a.MoveTo( actions[active_action].Button ) )
	{
		// Press the button
		press_button = true;
	}

	// Find the next action for the other robot
	for( size_t i = active_action+1; i < actions.size(); ++i )
	{
		if( actions[i].Robot == b.Id )
		{
			b.MoveTo( actions[i].Button );
			break;
		}
	}

	return press_button;
}

int Process()
{
	int num_actions;
	std::cin >> num_actions;

	std::vector<Action> actions;
	actions.reserve( num_actions );

	for( int i = 0; i < num_actions; ++i )
	{
		std::string robot;
		std::cin >> robot;

		int robot_num = robot == "O" ? 0 : 1;

		int button;
		std::cin >> button;

		Action action = { robot_num, button };
		actions.push_back( action );
	}

	Robot robots[2] = { Robot(0), Robot(1) };

	size_t active_action = 0;
	size_t num_steps = 0;
	while( active_action < actions.size() )
	{
		const Action & action = actions[active_action];

		if( UpdateRobots( robots[action.Robot], robots[1-action.Robot], active_action, actions ) )
			++active_action;

		++num_steps;
	}

	return num_steps;
}

int main(int argc, char* argv[])
{
	int num_tests;
	cin >> num_tests;
	
	for( int i = 0; i < num_tests; ++ i )
	{
		int steps = Process();
		printf( "Case #%d: %d\n", i+1, steps );
	}

	return 0;
}

