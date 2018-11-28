/*
 * googleC1.cpp
 *
 *  Created on: 22.05.2011
 *      Author: jet-lee
 */

#include <stdlib.h>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <vector>


int T;

using namespace std;


int main(int argc, char* argv[])
{

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	infile >> T;
	printf("Case %i \n",T);

	for(int t=0;t<T;t++)
	{

		int R;
		int C;

		infile >> R;
		infile >> C;
		printf("R = %i | C = %i \n",R,C);

		char input[R][C];

		// Save Matrix/Picture
		for(int r=0;r<R;r++)
		{
			infile >> &input[r][0];
			printf("Matrix: %s \n",input[r]);
		}


		/*******************************************************************/
		// Change Picture

		// Zeilen / ROWS
		for(int r=0;r<R;r++)
		{
			// Spalte / COLUMNS
			for(int c=0;c<C;c++)
			{
				if( (input[r][c]=='#') && (c+1 < C) && (r+1<R))
				{
					if( (input[r][c+1]=='#') && (input[r+1][c]=='#') && (input[r+1][c+1]=='#'))
					{
						input[r][c]='/';
						input[r][c+1]='\\';
						input[r+1][c]='\\';
						input[r+1][c+1]='/';
					}
				}
			}
		}

		/*******************************************************************/

		// Test result
		bool possible = true;
		for(int r=0; r<R; r++)
		{
			for(int c=0;c<C; c++)
			{
				if(input[r][c]=='#')
				{
					possible = false;
					break;
				}
			}
			if(possible == false)
			{
				break;
			}
		}


		/*******************************************************************/

		// Output
		printf("Case %i: \n",t+1);
		outfile << "Case #"<< t+1 <<":\n";

		if(possible)
		{
			for(int r=0;r<R;r++)
			{

				for(int c=0;c<C;c++)
				{
					outfile << input[r][c];
					printf("%c",input[r][c]);
				}
				printf("\n");
				outfile << "\n";
			}
		}
		else
		{
			outfile << "Impossible \n";
			printf("Impossible \n");
		}

	}

}
