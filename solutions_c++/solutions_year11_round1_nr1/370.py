// r1p1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;

	for(int i=0;i<T;i++)
	{
		double N;
		int Pd,  Pg;
		cin >> N;
		cin >> Pd;
		cin >> Pg;

		bool bflag = true;

		if (Pg == 100 && Pd != 100)
			bflag = false;

		if (Pg == 0 && Pd != 0)
			bflag = false;

		if (N < 100 && bflag)
		{
			bflag = false; 
			for(int j=1;j<=N;j++)
			{
				if ((j * Pd) % 100 == 0)
				{
					bflag = true;
					break;
				}
			}
		}


		if (bflag)
			printf("Case #%d: Possible\n", i+1);
		else
			printf("Case #%d: Broken\n", i+1);
	}

	return 0;
}

