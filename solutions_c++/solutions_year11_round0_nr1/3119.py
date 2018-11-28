#include <fstream>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define max(x, y) x>y?x:y
#define min(x, y) x<y?x:y


int main()
{
	ifstream input ("A-large.in");
	if(!input.is_open())
	{	
		cout << "error to open input file" << endl;
		return -1;
	}

	ofstream output ("A-large.out");
	if(!output.is_open())
	{
		cout << "unable to create the output file" << endl;
		return -1;
	}

	int i, j, t;
	int T, N;
	int dis, time;
	int robot1CurPos, robot2CurPos, curUsedTime;
	char who;
	pair<char, int> oneCommd;	
	
	
	input >> T;

	for(t = 0; t < T; ++t)
	{
		vector<pair<char, int>> command;
		input >> N;
		time = 0;
		curUsedTime = 0;
		robot1CurPos = 1;
		robot2CurPos = 1;

		for(i = 0; i < 2*N; i=i+2)
		{
			input >> who;
			input >> dis;

			oneCommd.first = who;
			oneCommd.second = dis;
			command.push_back(oneCommd);

		}

		for(i = 0; i < N; ++i)
		{
			curUsedTime = abs(robot1CurPos - command[i].second) + 1;
			time = time + curUsedTime;

			if(i == N-1)
				break;

			robot1CurPos = command[i].second;

			for(j = i+1; j < N; ++j)
			{
				if(command[i].first == command[j].first)
					continue;
				
				if(command[j].second > robot2CurPos)
					robot2CurPos = min(robot2CurPos + curUsedTime, command[j].second);
				else if(command[j].second < robot2CurPos)
					robot2CurPos = max(robot2CurPos - curUsedTime, command[j].second);
				else
					;

				break;
			}
		
			//if(i != 0 )
				if(command[i].first != command[i+1].first)
				{
					int tmp;
					tmp = robot1CurPos;
					robot1CurPos = robot2CurPos;
					robot2CurPos = tmp;
				}
		
		}

		output << "Case #" << t+1 << ": " << time << endl;
		//cout << "Case #" << t+1 << ": " << time << endl;

	}

	system("pause");
	return 0;
}