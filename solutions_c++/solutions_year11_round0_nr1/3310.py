
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	if (!in)
	{
		cout << "Cannot open file";
		return 1;
	}

	int T, N, buttonPos, bot;
	char r;
	
	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		in >> N;		
		queue<pair<int, int> > botActions[2];
		// read actions
		for (int n = 0; n < N; ++n)
		{			
			in >> r >> buttonPos;
			botActions[r == 'O' ? 0 : 1].push(pair<int, int>(buttonPos, n));
		}
		// simulate
		int time = 0;
		int sequence = 0;
		int botPos[2] = { 1, 1 };
		bool pressed = false;
		while (sequence != N)
		{
			time++;
			for (int bot = 0; bot < 2; ++bot)
			{
				if (botActions[bot].empty())
					continue;
				int destPos = botActions[bot].front().first;
				int seq = botActions[bot].front().second;
				if (botPos[bot] == destPos) // check if bot is in position
				{
					if (sequence == seq) // if it is its turn, press the button
					{
						pressed = true;
						botActions[bot].pop();
					}
				}
				else // move 1 step towards button
					botPos[bot] += destPos > botPos[bot] ? 1 : -1;				
			}
			if (pressed)
				sequence++;
			pressed = false;
		}
		printf("Case #%d: %d\n", i, time);
	}	

	return 0;
}