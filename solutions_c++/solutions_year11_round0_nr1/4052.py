#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

void main ()
{
	ifstream input;
	ofstream output;

	input.open("input.in");
	output.open("output.txt");

	int t, n;
	char bot;
	int pos;

	input >> t;

	for (int i = 0; i < t; i++)
	{
		input >> n;

		int curPosO = 1, curPosB = 1;
		bool turn;
		int elapsedTime, timeO = 0, timeB = 0;

		
		if ( n > 0 ) 
		{
			input >> bot;
			if (bot == 'O') turn = true;
			else turn = false;
			input >> elapsedTime;

			if (turn) timeO = curPosO = elapsedTime; 
			else timeB = curPosB = elapsedTime;
		}
		for (int i = 1; i < n; i++)
		{
			input >> bot >> pos;

			if (bot == 'O') 
			{
				int temp = timeO + abs(pos - curPosO) + 1;
				timeO = elapsedTime = max(temp, elapsedTime + 1);
				curPosO = pos;
			}
			else
			{
				int temp = timeB + abs(pos - curPosB) + 1;
				timeB = elapsedTime = max(temp, elapsedTime + 1);
				curPosB = pos;
			}
		}

		output << "Case #" << i + 1 << ": " << elapsedTime << endl;
	}
}