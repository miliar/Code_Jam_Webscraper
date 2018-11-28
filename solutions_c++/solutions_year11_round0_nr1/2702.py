#pragma once

#include <string>
#include <list>

class TestCase {

	struct RobotPosition  {
		RobotPosition(char r, int pos, RobotPosition *dep, RobotPosition *prev, int diffPrev) : 
	robot(r), position(pos), stepsToHere(0), diffToPrevious(diffPrev), dependsOn(dep), previousButton(prev) {}

		char robot;
		int position;
		int stepsToHere;
		int diffToPrevious;
		RobotPosition *dependsOn;
		RobotPosition *previousButton;
	};

	typedef std::list<RobotPosition *> PosList;

	PosList sequence;

	bool loadFromString(const std::string& str);

public:
	TestCase(const std::string& str);
	~TestCase();

	int solve();

};

