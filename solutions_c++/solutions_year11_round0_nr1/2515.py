#include <stdio.h>
#include <stdlib.h>
#include <new>
#include <limits.h>
#include <iostream>

using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void sortIt(int *anArray, int aCount)
{
  qsort (anArray, aCount, sizeof(int), compare);
}

#define max(x,y) ((x>y)?(x):(y))
#define min(x,y) ((x<y)?(x):(y))
#define abs(x) ((x<0)?(-(x)):(x))
int main()
{
	int nrCases;	
	cin >> nrCases;
	
	for (int caseNr = 0; caseNr < nrCases; caseNr++)
	{
		int nrButtons;
		cin >> nrButtons;
		
		int total = 0;
		int pos[2]= { 1, 1};
		int idle[2] = { 0, 0};
		
		for (int i = 0; i < nrButtons; i++)
		{
			char c;
			int buttonNr;
			cin >> c;
			cin >> buttonNr;
			
			int color = 0;
			
			if (c == 'O')
			{
				color = 1;
			}
			
			int steps = max(0, abs(pos[color] - buttonNr) - idle[color]) + 1;
			pos[color] = buttonNr;


			idle[color] = 0;
			idle[1-color] = idle[1-color] + steps;
			
			total = total + steps;
		}
		
		cout << "Case #" << caseNr + 1 << ": " << total << endl ;
		
	}
}
