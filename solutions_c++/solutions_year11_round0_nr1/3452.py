#include <fstream>
#include <string>
#include "stdlib.h"
#include <iostream>
#include <sstream>

using namespace std;

//PROBLEM LIMITS
#define LIMIT_N 100

string cutNext (string line, int& start, string delimiter);

int main (void)
{
	//make input/output streams
	fstream input ("A-large.in");//REMEMBER TO CHANGE
	fstream output ("output.out");

	//make string to hold the contents of each line
	string line;

	//get the number of cases
	getline (input, line);
	int cases = atoi (line.c_str());
	
	//go through each case
	for (int caseno = 1; caseno <= cases; caseno++)
	{
		//how many seconds have elapsed
		int seconds = 0;

		//what buttons have been pressed and by which robot
		int buttonsO[LIMIT_N];
		int buttonsB[LIMIT_N];
		//the last index of the pressed button
		int lastO = -1;
		int lastB = -1;

		for (int j = 0; j < LIMIT_N; j++)//set all to 0
		{
			buttonsO[j] = -1;
			buttonsB[j] = -1;
		}
	

		getline (input, line);
		int startPos = 0;
		string v = cutNext (line,startPos," ");
		int N = atoi (v.c_str());

		//get the list of commands
		int commands [2][LIMIT_N];
		//read each command in the line
		for (int i = 0; i < N; i++)
		{
			v = cutNext (line, startPos, " ");
			if (v.compare("O") == 0)
			{
				commands[0][i] = 1;
			}
			else
				commands[0][i] = 2;

			v = cutNext (line, startPos, " ");
			commands[1][i] = atoi (v.c_str())-1;//convert to position in array - robots now start at 0
		}

		int command = 0;//what command we are currently up to

		//positions of the robots
		int positionO = 0;
		int positionB = 0;
		//actions the robots will perform
		int actionO;
		int actionB;

		//LIST OF ACTIONS//
		// 0 - stay put
		// 1 - press putton
		// 2 - move forward
		// 3 - move back

		//perform actions until all commands are completed
		while (command < N)
		{
			////////////////////////////
			//Decide action for orange//
			////////////////////////////

			//get the next orange command : -1 for mo more commands
			int commandO = -1;
			for (int ii = command; ii < N; ii++)
			{
				if (commands[0][ii] == 1)
				{
					commandO = ii;
					break;
				}
			}

			if (commandO == -1) //if there are no more commands for orange
				actionO = 0;
			else
			{
				if (commands[1][commandO] == positionO)//if standing on the right button
				{
					//see if the button before it has been pressed
					if (commandO > 0) //if not the first command
					{
						if (commands[0][commandO-1] == 1)//if the previous command was for orange
						{
							if (buttonsO[lastO] == commands[1][commandO-1] && commandO == command)//if the last button pressed by orange was the prev for this
								actionO = 1;
							else
								actionO = 0;
						}
						else //if it was for blue
						{
							if (buttonsB[lastB] == commands[1][commandO-1] && commandO == command)
								actionO = 1;
							else 
								actionO = 0;
						}
					}
					else
						actionO = 1;
				}

				if (commands[1][commandO] < positionO)//too far forward
					actionO = 3;

				if (commands[1][commandO] > positionO)//too far back
					actionO = 2;
			}

			////////////////////////////
			//Decide action for blue//
			////////////////////////////

			//get the next blue command : -1 for mo more commands
			int commandB = -1;
			for (int ii = command; ii < N; ii++)
			{
				if (commands[0][ii] == 2)
				{
					commandB = ii;
					break;
				}
			}

			if (commandB == -1) //if there are no more commands for blue
				actionB = 0;
			else
			{
				if (commands[1][commandB] == positionB)//if standing on the right button
				{
					//see if the button before it has been pressed
					if (commandB > 0) //if not the first command
					{
						if (commands[0][commandB-1] == 1)//if the previous command was for orange
						{
							if (buttonsO[lastO] == commands[1][commandB-1] && commandB == command)//if the last button pressed by orange was the prev for this
								actionB = 1;
							else
								actionB = 0;
						}
						else //if it was for blue
						{
							if (buttonsB[lastB] == commands[1][commandB-1] && commandB == command)
								actionB = 1;
							else 
								actionB = 0;
						}
					}
					else
						actionB = 1;
				}

				if (commands[1][commandB] < positionB)//too far forward
					actionB = 3;

				if (commands[1][commandB] > positionB)//too far back
					actionB = 2;
			}

			///////////////////
			//Perform actions//
			///////////////////
			
			//Orange action
			switch (actionO)
			{
			case 1://press the button
				lastO++;
				buttonsO[lastO] = positionO;
				command++;
				break;
			case 2://move forward
				positionO++;
				break;
			case 3://move back
				positionO--;
				break;
			}

			//Blue action
			switch (actionB)
			{
			case 1://press the button
				lastB++;
				buttonsB[lastB] = positionB;
				command++;
				break;
			case 2://move forward
				positionB++;
				break;
			case 3://move back
				positionB--;
				break;
			}

			seconds ++;//time has moved forward
		}
		cout << "Case #" << caseno << ": " << seconds << endl;
		output << "Case #" << caseno << ": " << seconds << endl;
	}

	//close files and return
	input.close();
	output.close();
	return 0;
}

//returns the next string after the start till the delimiter
string cutNext (string line, int& start, string delimiter)
{
	int pos;

	pos = line.find (delimiter, start);
	string cut = line.substr (start,pos-start);
	start = pos+1;

	return cut;
}