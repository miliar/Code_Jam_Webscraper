#include<iostream>

using namespace std;

void printCommand(int button, int robot);

int main()
{
	int t;
	cin >> t;

	const int BUTTON = 0;
	const int ROBOT = 1;

	int commands[101][2];

	for (int c = 0; c < t; c++)
	{
		int n;
		cin >> n;
		char r;

		for (int i = 0; i < n; i++)
		{
			cin >> r;
			cin >> commands[i][BUTTON];

			if (r == 'O')
				commands[i][ROBOT] = 0;
			else
				commands[i][ROBOT] = 1;
		}

		int time[2] = {0, 0};
		int pos[2] = {1, 1};

		for (int i = 0; i < n; i++)
		{
			//calculate min time needed
			int min = commands[i][BUTTON] - pos[commands[i][ROBOT]];
			if (min < 0)
				min *= -1;

			//Add time to press the button
			min++;

			time[commands[i][ROBOT]] += min;

			pos[commands[i][ROBOT]] = commands[i][BUTTON];

			//if we have to wait for the other robot, add the wait time
			if (i > 0 && (commands[i][ROBOT] != commands[i-1][ROBOT]))
			{
				if (time[commands[i][ROBOT]] <= time[commands[i-1][ROBOT]])
					time[commands[i][ROBOT]] = time[commands[i-1][ROBOT]]+1;
			}
		}

		int max;
		if (time[0] > time[1])
			max = time[0];
		else
			max = time[1];


		//Output
		cout << "Case #" << (c+1) << ": " << max << endl;
	}
	return 0;
}

void printCommand(int button, int robot)
{
	char c;
	if (robot == 0)
		c = 'O';
	else
		c = 'B';

	cout << "Robot " << c << " has to press button " << button << endl;
}
