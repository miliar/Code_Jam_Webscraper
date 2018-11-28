// TaskA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <list>
#include <queue>
using namespace std;
/// Robots

struct Command
{
	int idx;
	int button;
	Command(int in_idx, int in_btn)
	{
		idx = in_idx;
		button = in_btn;
	}
};

int UpdateQueue(queue<Command>* in_queue, int pos, bool myTurn)
{
	int res = pos;
	/// Do we stay in front of button?
	if(pos == in_queue->front().button)
	{
		/// Push if it is time to
		if(myTurn)
		{
			//cout<<"push button!";
			/// Assume that we push button here
			in_queue->pop();
		}
			//cout<<"I am staying";
		/// Otherwise do nothing
	}else
	{
		if(pos < in_queue->front().button)
		{
			res++;
			//cout<<"step forward";
		}
		else
		{
			res--;
			//cout<<"step back";
		}
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("A-large.in");
	ofstream output;
	output.open("TaskA.out");
	if(input.is_open())
	{
		int size;
		input>>size;
		const int MAX_LINE_SIZE = 5000;
		char line[MAX_LINE_SIZE];
		input.getline(line, MAX_LINE_SIZE);
		for(int i = 0; i<size; i++)
		{
			//input.getline(line, MAX_LINE_SIZE);
			//stringstream ss(line);
			queue<Command> blueQueue;
			queue<Command> orangeQueue;
			int index = 0;
			int count;
			input >> count;
			for(int j = 0; j<count; j++)
			{
				queue<Command>* pCurrent;
				char c;
				input >> c;
				if(c == 'O')
					pCurrent = &orangeQueue;
				else
					pCurrent = &blueQueue;
				int newButton;
				input >> newButton;
				pCurrent->push(Command(index, newButton));
				index++;
			}
//			assert(index == tmp);
			/// Now solve task
			int bluePos = 1;
			int orangePos = 1;
			int stepsCount = 0;
			bool blueTurn;
			bool orangeTurn;
			//cout<<"blue       ||   orange";
			while(!blueQueue.empty() || !orangeQueue.empty())
			{
				if(orangeQueue.empty())
					blueTurn = true;
				else if(blueQueue.empty())
					blueTurn = false;
				else
					blueTurn = (blueQueue.front().idx < orangeQueue.front().idx);
				orangeTurn = !blueTurn;
				/// Frist step if possible
				if(!blueQueue.empty())
				{
					bluePos = UpdateQueue(&blueQueue, bluePos, blueTurn);
				}
				/// Frist step if possible
				if(!orangeQueue.empty())
				{
					orangePos = UpdateQueue(&orangeQueue, orangePos, orangeTurn);
				}
				//cout<<endl;
				stepsCount++;
			}
			/// output stepsCount:
			output<<"Case #"<<i+1<<": "<<stepsCount<<endl;
		}
		input.close();
		output.close();
	}
	else
	{
		//cout<<"Input file not found";
		return 1;
	}
	return 0;
}

