////////////////////////////////////////////////////////
///////    Theme Park
///////    A empty win32 console project
///////    Language : C++
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
///////		Constant
///////////////////////////////////////////////////////
#define INPUT_PATH "ThemePark.in"  // input file name
#define OUTPUT_PATH "ThemePark.out" // output file name


///////////////////////////////////////////////////////
///////		Using library
///////////////////////////////////////////////////////
#include <iostream>
#include <fstream>
using namespace std;


///////////////////////////////////////////////////////
///////		Global variable
///////////////////////////////////////////////////////

ifstream fileInput; // input stream
ofstream fileOutput; // output stream
int numberCase; // number of test
int R,K,N; // input data
int client[1000];
int clientLoop[1000];
int support,totalClient; // client in a round
int index; // index of first client of a round
double amount[1000];
double total;



///////////////////////////////////////////////////////
///////		Sub function
///////////////////////////////////////////////////////



///////////////////////////////////////////////////////
///////		Main function
///////////////////////////////////////////////////////

void main()
{
	fileInput.open(INPUT_PATH);
	fileOutput.open(OUTPUT_PATH);
	fileInput >> numberCase;
	index = 0;
	for (int i = 0; i< numberCase; i++)
	{
		totalClient = 0;
		fileInput >> R >> K >> N;
		for (int j=0; j<N; j++)
		{
			fileInput >> client[j];
			totalClient += client[j];
			amount[j] = 0;
		}
		if (totalClient <= K)
			total = totalClient * R;
		else
		{
			int k = 0;
			total = 0;
			index = 0;
			for (; k<R; k++)
			{
				support = 0;
				amount[index] = total;
				clientLoop[index] = k;
				while (support <K && support <totalClient) 
				{
					if (support + client[index] <= K && support + client[index]<=totalClient)
					{
						support += client[index];
						total += client[index];
						index = (index + 1)%N;
					}
					else break;
				}
				if (amount[index] != 0) break;
			}
			if (k<R)
			{
				k++;
				total = total + (total-amount[index])*((R-k)/(k-clientLoop[index]));
				k+= ((R-k)/(k-clientLoop[index]))*(k-clientLoop[index]);
			}
			for (; k<R; k++)
			{
				support = 0;
				while (support <K && support <totalClient) 
				{
					if (support + client[index] <= K && support + client[index]<=totalClient)
					{
						support += client[index];
						total += client[index];
						index = (index + 1)%N;
					}
					else break;
				}
			}
		}
		fileOutput << "Case #" << i+1 << ": " << total << endl;
	}
	fileInput.close();
	fileOutput.close();
}