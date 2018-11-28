


#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;


char pictures[50][50];
int num_row;
int num_column;
string str;

int
ifPossible()
{
	for (int i = 0 ; i < num_row ; i++)
	{
		for (int j = 0 ; j < num_column ; j++)
		{
			if (pictures[i][j] == '#')
			{
				if ((pictures[i][j + 1] == '#') 
					&& (pictures[i + 1][j] == '#') 
					&& (pictures[i + 1][j + 1] == '#'))
				{
					pictures[i][j] = '/';
					pictures[i][j + 1] = '\\';
					pictures[i + 1][j] = '\\';
					pictures[i + 1][j + 1] = '/';
				} else 
					return 0;
			}
		}
	}
	return 1;
}

int main ()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.txt");
	outFile.open("output.txt");
	int num_cases;
	inFile >> num_cases;
	
	for (int curr_case = 0 ; curr_case < num_cases ; curr_case++ )
	{
		memset(pictures, 0, sizeof(pictures));
		inFile >> num_row;
		inFile >> num_column;
		
		for (int i = 0 ; i < num_row ; i++)
		{
			inFile >> str;
			for (int j = 0 ; j < num_column ; j++)
			{
				pictures[i][j] = str[j];
			}
		}

		if (ifPossible() == 0)
		{
			outFile << "Case #" << curr_case + 1 << ": " << endl;
			outFile << "Impossible" << endl;
		}
		else
		{
			outFile << "Case #" << curr_case + 1 << ": " << endl;
			for (int i = 0 ; i < num_row ; i++)
			{
				for (int j = 0 ; j < num_column ; j++)
					outFile << pictures[i][j];
				outFile << endl;
			}
		}
	}

	return 0;
}

