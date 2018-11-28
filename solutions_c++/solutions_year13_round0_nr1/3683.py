// GCJ13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	  ifstream in("A-large.in" );      // A-tiny-practice.in    // A-small-practice.in    // A-large-practice.in
	  ofstream outfile("A-large.out");
	  string line;
	  //int tc; scanf("%d", &tc);
	  getline( in, line );
	  int tc = atoi( line.c_str() );
	  
	  for(int tci = 0; tci < tc; tci++)
	  {
		char rowC[4] = {0};
		char rowS[4] = {0};
		char colC[4] = {0};
		char colS[4] = {0};
		char diagC[2] = {0};
		char diagS[2] = {0};
		char empty = 0;

		for(int ri = 0; ri < 4; ri++)
		{
			getline( in, line );
			for(int ci = 0; ci < 4; ci++)
			{

				//char c = 'O';
				char c = line[ci];
				int rowIndex = ri;
				int colIndex = ci;
				int diagIndex = ri == ci ? 0 : -1;
				if(diagIndex == -1)
					diagIndex = ri + ci == 3 ? 1 : -1;

				if(c == 'O')
				{
					rowC[rowIndex]++;
					colC[colIndex]++;
					if(diagIndex != -1)
					{
						diagC[diagIndex]++;
					}
				}
				else if(c == 'X')
				{
					rowS[rowIndex]++;
					colS[colIndex]++;
					if(diagIndex != -1)
					{
						diagS[diagIndex]++;
					}
				}
				else if(c == 'T')
				{
					rowS[rowIndex]++;
					colS[colIndex]++;
					if(diagIndex != -1)
					{
						diagS[diagIndex]++;
					}
					rowC[rowIndex]++;
					colC[colIndex]++;
					if(diagIndex != -1)
					{
						diagC[diagIndex]++;
					}
				}
				else
				{
					empty++;
				}
			}
		}
		getline( in, line );

		//analyze
		bool haveWinner = false;
		for(int i = 0; i<4;i++)
		{
			if(rowC[i] == 4 || colC[i] == 4 || diagC[i%2] == 4) 
			{
					cout<<"Case #"<<tci+1<<": O won"<<endl;
					//printf("Case #%d: O won", tci);
					haveWinner = true;
					break;
			}
			if(rowS[i] == 4 || colS[i] == 4 || diagS[i%2] == 4)
			{
				cout<<"Case #"<<tci+1<<": X won"<<endl;
				//printf("Case #%d: X won", tci);
				haveWinner = true;
				break;
			}
		}
		if(!haveWinner)
			if(empty == 0)
				cout<<"Case #"<<tci+1<<": Draw"<<endl;
				//printf("Case #%d: Draw", tci);
			else
				cout<<"Case #"<<tci+1<<": Game has not completed"<<endl;
				//printf("Case #%d: Game has not completed", tci);		
	
  }
}

