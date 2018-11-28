#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
// Read from file
#if 1
	ifstream readStream;
	ofstream writeStream;

	readStream.open("A-large.in", ios::in);
	writeStream.open("A-large.out", ios::out);
#endif

	char temp[1200];

	readStream.getline(temp, 1200, '\n');

	int i, b;
	vector<int> buttonB;
	vector<int> buttonO;
	int nCase = atoi(temp);

	for(i=0; i<nCase; i++)
	{
		buttonB.clear();
		buttonO.clear();
		readStream.getline(temp, 1200, '\n');

		char *splitted;
		splitted = strtok(temp," ");
		int nButton = atoi(splitted);

		int time = 0;
		int freeTime = 0;
		int useTime = 0;
		int currB = 1;
		int currO = 1;
		char lastRobot = 'X';

		for(b=0; b<nButton; b++)
		{
			splitted = strtok(NULL," ");
			char robot = splitted[0];

			splitted = strtok(NULL," ");
			int button = atoi(splitted);

			if(robot == 'B')
			{
				useTime = abs(button - currB) + 1;
				currB = button;
			}
			else if(robot == 'O')
			{
				useTime = abs(button - currO) + 1;
				currO = button;
			}

			if(lastRobot == robot)
			{
				time += max(1, useTime);
				freeTime += max(1, useTime);
			}
			else
			{
				time += max(1, useTime - freeTime);
				freeTime = max(1, useTime - freeTime);
			}

			lastRobot = robot;
		}

		writeStream<<"Case #"<<(i+1)<<": "<<time<<"\n";
	}

	readStream.clear();
	readStream.close();

	writeStream.clear();
	writeStream.close();

	return 0;
}

