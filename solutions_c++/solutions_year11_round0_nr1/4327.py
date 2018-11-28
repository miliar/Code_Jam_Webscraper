#include <cstdio>
#include <iostream>
#include <vector>
#include <cassert>
#include <queue>

enum {
	OrangeRobot,
	BlueRobot
};

using namespace std;

class Command {
public:
	Command() {}
	Command(char robot, int button)
		: button(button)
	{
		if(robot == 'O')
			this->robot = OrangeRobot;
		else if(robot == 'B')
			this->robot = BlueRobot;
		else
			assert(false);
	}
	int robot;
	int button;
};

Command getNextButton(vector<Command> &cmdlist, int robot, bool &cmdExist)
{
	assert(cmdlist.size() > 0);
	cmdExist = false;
	
	while(cmdlist.empty() == false)
	{
		vector<Command>::iterator it;
		for(it = cmdlist.begin() ; it != cmdlist.end() ; it++)
		{
			Command &cmd = *it;
			if(cmd.robot == OrangeRobot)
			{
				cmdExist = true;
				cmdlist.erase(it);
				return cmd;
			}
		}
	}
}

queue<int> getRobotPathList(const vector<Command> &cmdlist, int robot)
{
	queue<int> result;
	for(int i = 0 ; i < cmdlist.size() ; i++)
	{
		const Command &cmd = cmdlist[i];
		if(cmd.robot == robot)
			result.push(cmd.button);
	}
	return result;
}

int calcPath(vector<Command> &cmdlist)
{
	queue<int> orangePathList = getRobotPathList(cmdlist, OrangeRobot);
	queue<int> bluePathList = getRobotPathList(cmdlist, BlueRobot);
	int orangePos = 1;
	int bluePos = 1;
	int turn = 0;
	while(cmdlist.empty() == false)
	{
		Command &cmd = cmdlist.front();

		bool orangePushOccur = false;
		bool bluePushOccur = false;
		//버튼을 누를수 있는 경우, 버튼을 누르기
		if(cmd.robot == OrangeRobot)
		{
			if(cmd.button == orangePos)
			{
				vector<Command>::iterator it = cmdlist.begin();
				cmdlist.erase(it);
				orangePathList.pop();
				orangePushOccur = true;
			}
		}
		//버튼 누르기는 동시에 안된다
		if(cmd.robot == BlueRobot && orangePushOccur == false)
		{
			if(cmd.button == bluePos)
			{
				vector<Command>::iterator it = cmdlist.begin();
				cmdlist.erase(it);
				bluePathList.pop();
				bluePushOccur = true;
			}
		}

		int orangeTarget = orangePos;
		if(orangePathList.size() > 0)
			orangeTarget = orangePathList.front();
		int blueTarget = bluePos;
		if(bluePathList.size() > 0)
			blueTarget = bluePathList.front();

		//target향해서 이동
		if(orangePushOccur == false)
		{
			if(orangePos > orangeTarget)
				orangePos--;
			else if(orangePos < orangeTarget)
				orangePos++;
		}

		if(bluePushOccur == false)
		{
			if(bluePos > blueTarget)
				bluePos--;
			else if(bluePos < blueTarget)
				bluePos++;
		}

		turn++;
		//printf("turn:%d : %d / %d\n", turn, orangePos, bluePos);
	}
	return turn;
}


int main()
{
	//hard coding
	vector<Command> cmdlist;
	/*
	Command c1('O', 2);
	Command c2('B', 1);
	Command c3('B', 2);
	Command c4('O', 4);
	cmdlist.push_back(c1);
	cmdlist.push_back(c2);
	cmdlist.push_back(c3);
	cmdlist.push_back(c4);
	*/
	/*
	Command c1('B', 2);
	Command c2('B', 1);
	cmdlist.push_back(c1);
	cmdlist.push_back(c2);
	*/
	/*
	Command c1('O', 5);
	Command c2('O', 8);
	Command c3('B', 100);
	cmdlist.push_back(c1);
	cmdlist.push_back(c2);
	cmdlist.push_back(c3);
	*/
	

	
	//read input data
	int numTestCase;
	cin >> numTestCase;

	for(int i = 0 ; i < numTestCase ; i++)
	{
		int numCommand;
		cin >> numCommand;

		vector<Command> cmdlist;

		for(int j = 0 ; j < numCommand ; j++)
		{
			char robot;
			int button;
			cin >> robot;
			cin >> button;

			Command cmd(robot, button);
			cmdlist.push_back(cmd);
		}

		int result = calcPath(cmdlist);
		printf("Case #%d: %d\n", i+1, result);
	}
	return 0;
}