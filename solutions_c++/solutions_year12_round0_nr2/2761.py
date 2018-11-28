// Dancing With the Googlers2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * inFile = fopen("input.txt", "r");
	FILE * outFile = fopen("output.txt", "w");

	int n, i, j, m, s, p, w, t, c, ans;
	fscanf(inFile, "%d", &n);
	for(i = 0; i < n; i++)
	{
		fscanf(inFile, "%d %d %d", &m, &s, &p);
		ans = 0;
		for(j = 0; j < m; j++)
		{
			fscanf(inFile, "%d", &c);
			int t = c % 3;
			int w = c / 3;
			switch(t)
			{
			case 0:
				if(w >= p)
				{
					ans++;
				}
				else if (w == p - 1 && s > 0 && w - 1 > 0)
				{
					s--;
					ans++;
				}
				break;
				
			case 1:
				if(w + 1 >= p)
				{
					ans++;
				}
				break;

			case 2:
				if(w + 1 >= p)
				{
					ans++;
				}
				else if (w + 2 >= p && s > 0)
				{
					s--;
					ans++;
				}
				break;
			}
		}
		fprintf(outFile, "Case #%d: %d\n", i+1, ans);
	}
	return 0;
}

