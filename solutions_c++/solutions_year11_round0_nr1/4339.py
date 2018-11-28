// Bot Trust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

char Twho[200];
int  Tbutton[200];

int max(int a, int b) { return a > b ? a : b; }

int result(int n)
{
	int Bpos = 1;
	int Opos = 1;
	int res = 0;
	int i;

	int  timeGiven = 0;
	i = 0;
	while(i < n)
	{
		char c = Twho[i];
		
		int myTime = 0;
		for( ; i<n && Twho[i] == c; i++)
		{
			int current = (c == 'B' ? Bpos : Opos);
			myTime += max(0, abs(current-Tbutton[i]) - timeGiven) + 1;
			timeGiven = 0;
			if(c=='B')
				Bpos = Tbutton[i];
			else
				Opos = Tbutton[i];
		}
		res += myTime;
		timeGiven = myTime;
	}

	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tests, n;
	scanf("%d", &tests);
	for(int i = 0; i < tests; i++)
	{
		scanf("%d", &n);
		for(int j = 0; j < n; j++)
		{
			scanf(" %c %d", &Twho[j], &Tbutton[j]);
		}
		printf("Case #%d: %d\n", i+1, result(n));
	}


	return 0;
}

