// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <assert.h>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int numCase, N,P,S;

	/*while(true)
	{
		int i =1;
		i++;
	}*/

	cin >> numCase;
	for (int i = 0; i < numCase; i++)
	{
		int result = 0;
		cin >> N >> S >> P;
		
		for (int j = 0; j < N; j++)
		{
			int value;
			cin >> value;

			if(value==29)
				result++;
			else if(value==0)
			{
				if(P==0)
					result++;
			}
			else if(value%3 == 0)
			{
				int a = value/3;
				if(a >= P)
					result++;
				else if(a+1 >=P && S > 0)
				{
					result++;
					S--;
				}
			}
			else if(value%3 == 1)
			{
				int a = value/3;
				if(a+1 >=P)
					result++;
			}
			else
			{
				int a = value/3;
				if(a+1 >=P)
					result++;
				else if(a+2 >=P && S > 0)
				{
					result++;
					S--;
				}
			}
		}
		
		cout << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}

