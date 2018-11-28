// go.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

	cin >> T;
	for(int i=0;i<T;i++)
	{
		int B_Loc = 1, O_Loc = 1;
		int B_Time = 0, O_Time = 0;
		int nCost = 0;

		int N;
		cin >> N;
		for(int j=0;j<N;j++)
		{
			char cRobot;
			int nTarget;
			int nUsedTime;
			cin >> cRobot;
			cin >> nTarget;

			switch(cRobot)
			{
			case 'O':
				nUsedTime = abs(nTarget - O_Loc) - O_Time;
				if (nUsedTime < 0) 
					nUsedTime = 0;
				nUsedTime++;
				O_Time = 0;
				B_Time += nUsedTime;
				nCost += nUsedTime;
				O_Loc = nTarget;

				break;
			case 'B':
				nUsedTime = abs(nTarget - B_Loc) - B_Time;
				if (nUsedTime < 0) 
					nUsedTime = 0;
				nUsedTime++;
				B_Time = 0;
				O_Time += nUsedTime;
				nCost += nUsedTime;
				B_Loc = nTarget;
				break;
			}
		}

		printf("Case #%d: %d\n", 1+i, nCost);
	}
	
	return 0;
}

