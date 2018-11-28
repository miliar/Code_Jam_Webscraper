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
#include <sstream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int numCase, A,B;

	/*while(true)
	{
		int i =1;
		i++;
	}*/

	cin >> numCase;
	char buffer[20];
	for (int i = 0; i < numCase; i++)
	{
		int result = 0;
		cin >> A >> B;
		
		for (int N = A; N < B; N++)
		{
			string strN;
			
			stringstream strStream;
			strStream << N;
			strStream >> buffer;
			strN = buffer;

			set<int> Nsolutions;
			for(int j=1;j<strN.length();j++)
			{
				int M = 0;
				string strM = strN.substr(j)+strN.substr(0,j);
				stringstream mStream;
				mStream << strM.c_str();
				mStream >> M;
				if(N<M && M<=B)
					Nsolutions.insert(M);
			}

			result+=Nsolutions.size();
		}
		
		cout << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}

