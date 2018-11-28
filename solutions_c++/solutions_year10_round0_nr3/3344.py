/*
 * Theme Park.cpp
 * -------------------------------
 * 
 *
 *
 */

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
	//Input and output streams
	ifstream input;
	ofstream output;

	int location, //Who's next in line?
		start_loc, //What location did the loading start at (we can't use a group twice on the same run
		space, //How much space is left in the coaster?
		money, //Keeps track of how much money made
		counter, counter2, //Counter variables
		cases, //Number of test cases
		runs, //Number of runs the coaster will make
		capacity, //Number of people it can hold
		groups_num; //Number of groups

	int* groups; //Pointer to dynamic array of group sizes

	bool full, //Keep track of state of coaster
		 done, //Keep track of if runs are complete
		 loop; //Keep track of if we are back to original person during loading

	input.open("C-small.in"); //Open the input
	output.open("output.txt"); //Open the output

	if(input.is_open() && output.is_open()) //Make sure the files opened correctly
	{
		input >> cases; //Input the cases

		for(counter = 0; counter < cases; counter ++)
		{
			input >> runs;
			input >> capacity;
			input >> groups_num;
			
			groups = new int[groups_num];
			for(counter2 = 0; counter2 < groups_num; counter2++)
			{
				input >> groups[counter2];
			}

			money = 0;
			done = false;
			location = 0;
			while(!done)
			{
				space = capacity;
				if(runs > 0)
				{
					full = false;
					loop = false;
					start_loc = location;
					while(!full)
					{
						if(groups[location] <= space && !loop)
						{
							space -= groups[location];
							money += groups[location];
							if(location < groups_num-1)
							{
								location++;
								if(location == start_loc)
								{
									loop = true;
								}
							}
							else
							{
								location = 0;
								if(location == start_loc)
								{
									loop = true;
								}
							}
						}
						else
						{
							full = true;
						}
					}
					runs--;
				}
				else
				{
					done = true;
				}
			}
			output << "Case #" << counter+1 << ": " << money << endl;

			delete [] groups;
		}
	}
	else
	{
		cout << "Could not open files!" << endl;
	}

	input.close();
	output.close();

	return 0;
}

