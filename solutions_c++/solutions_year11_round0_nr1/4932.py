#include <iostream>
#include <fstream>
#include<stdlib.h>
#include<string.h>

using namespace std;

//Function declarations

int power(int,int);
void OutputWriter(int *results, int length);
void fileError(int error);
void OutputPrinter();
void arrayPrinter(int *array, int length);
void ResetArray(int *array, int array_length);
int FindNext(int *array, int startpos, int length);

int programlogic(int*,int*,int);

//main begins
int main(int argc, char *argv[])
{
	if(argc < 2)
	{
		fileError(0);
	}

	//command line input
	string fname = argv[1];
	ifstream in(fname.data());

	if(!in)
	{
		fileError(1);
	}

	int testcases = 0;
	int numbuttons = 0;
   	char str[255];


	in.getline(str, 255);
	testcases = atoi(str);

	int results[testcases];		//final output array containing the time values

	int seconds=0;
	char *c;
	for(int j=0; j<testcases; j++)
	{
		in.getline(str, 255);
		c = strtok(str, " ");
		numbuttons = atoi(c);
		int orangebutton[numbuttons];
		int bluebutton[numbuttons];

		ResetArray(orangebutton, numbuttons);
		ResetArray(bluebutton, numbuttons);

		//populating the orangebutton and bluebutton arrays
		for(int m=0; m < numbuttons; m++)			
		{
			c = strtok(NULL, " ");

			if( *c == 'O')
			{
				orangebutton[m] = atoi(strtok(NULL, " "));
				cout << "o:" << orangebutton[m] << ",";
			}

			else if ( *c == 'B')
			{
				bluebutton[m] = atoi(strtok(NULL, " "));
				cout << "b:" << bluebutton[m] << ",";
			}
		}

		seconds = programlogic(orangebutton, bluebutton, numbuttons);
	
		cout << endl;
		results[j] = seconds;
		seconds = 0;		//resetting the timer

	}
	OutputWriter(results, testcases);
	in.close();
	return 0;
}

//program logic function
int programlogic(int *orangebuttons, int *bluebuttons, int numbuttons)
{
	int seconds = 0;
	
	//initial positions of the two robots
	int o_initial = 0;
	int b_initial = 0;			

	// next position for O or B to visit	
	int o_next = 0;
	int b_next = 0;

	// current position of O and B
	int o_current = 1;
	int b_current = 1;
	
	o_next = FindNext(orangebuttons, o_initial, numbuttons);
	b_next = FindNext(bluebuttons, b_initial, numbuttons);	

	int i=0;
	while(i<numbuttons)
		{
			if(orangebuttons[i] !=0)
			{	
				//orange begins
				int j;
				int target = orangebuttons[i];
				
				if(o_current<target)
				{
					while(o_current<target)
					{
						//move orange one step
						o_current++;
						
						if(bluebuttons[b_next] > b_current)		//move b forward if required
						{
							b_current++;
							//else hold b's position
						}
						if(bluebuttons[b_next] < b_current)		//move b backward if required
						{
							b_current--;
							//else hold b's position
						}
						seconds++;					//increment the timer
					}
				}
			
				if(o_current > target)
				{
					while(o_current > target)				// move o one step back 
					{
						o_current--;					
						if(bluebuttons[o_next] > b_current)		//move b forward if required
						{
							b_current++;
							//else hold b's position
						}
						else if(bluebuttons[b_next] < b_current)	//move b backward if required
						{
							b_current--;
						}
						seconds++;
					}
				}
				if(o_current==target)					//if current and target position same, press button
				{
					seconds++;					//push button
					if(bluebuttons[b_next] > b_current)		//move b if required
					{
						b_current++;
					}

					else if(bluebuttons[b_next] < b_current)		//move b if required
					{
						b_current--;
					}
					o_next = FindNext(orangebuttons, o_next+1, numbuttons);//next position for orange
				}	
			}

			else if(bluebuttons[i] !=0)				//blue robot operation begins
			{
				int j;
				int target = bluebuttons[i];
				
				if(b_current < target)
				{
					while(b_current<target)
					{
						//move blue one step
						b_current++;
						if(orangebuttons[o_next] > o_current)		//move o forward if required
						{
							o_current++;
							//else hold o's position
						}
						if(orangebuttons[o_next] < o_current)		//move o backward if required
						{
							o_current--;
							//else hold o's position
						}
						seconds++;					//increment the timer
					}
				}

				if(b_current > target)
				{
					while(b_current > target)				// move b one step back 
					{
						b_current--;					
						if(orangebuttons[o_next] > o_current)		//move o forward if required
						{
							o_current++;
							//else hold o's position
						}
						else if(orangebuttons[o_next] < o_current)	//move o backward if required
						{
							o_current--;
						}
						seconds++;
					}
				}
			
				if(b_current==target)					//if current and target position same, press button
				{
					seconds++;					//push button
					if(orangebuttons[o_next] > o_current)		//move o forward if required
					{
						o_current++;
					}
					if(orangebuttons[o_next] < o_current)		//move o backward if required
					{
						o_current--;
					}
				
					b_next = FindNext(bluebuttons, b_next+1, numbuttons);//next position for blue
				}	
			}
			i++;
		}
	return seconds;
}

int FindNext( int *array,int startpos, int length_of_array)
{
	int i;
	
	for(i=startpos; i < length_of_array; i++)
	{
		if(array[i] !=0)
		break;
	}
	return i;
}

void ResetArray(int *array, int len)
{
	for(int a=0; a<len;a++)
	array[a] = 0;
	return;
}
void arrayPrinter(int *array,int l)
{
	for(int a=0; a<l;a++)
	cout << array[a] << endl;
	return;
}

int power( int exponent, int base)
{
	int sum=1;
	for(int i=1; i<=exponent;i++)
	sum = 2 * sum;
	return sum;
}

void OutputWriter(int *seconds, int length)
{
	ofstream output("result.txt");
	int counter = 1;
	for(int i= 0; i < length; i++)
		{
			output << "Case #" << counter <<": " << seconds[i] << endl;
			counter++;
		}

	output.close();
	OutputPrinter();
	return;
}
void OutputPrinter()
{
	char line[255];
	ifstream test("result.txt");
	cout << "-----------Output-----------" << endl;
	while(test)
	{
		test.getline(line, 255);
		cout << line << endl;
	}
	test.close();
	return;
}
void fileError(int error)
{
	if(error == 0)
	{
		cout << " no input file" << endl;
	}
	else if(error == 1)
	{	
		cout << "Cannot open file." << endl;
	}
	exit (1);
}

