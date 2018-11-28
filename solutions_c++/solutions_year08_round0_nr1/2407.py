// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	string temp;
	int N, S, Q;
	int i, j, flag, result;
	map<string, int> engine; 
	ifstream In("A-large.in.txt");
	ofstream Out("output.txt");
	if ( !In )
	{
		cout<< "OPEN txt ERROR"<< endl;
		exit(0);
	}

	In >> N;
	for (i = 0; i < N; i++)
	{
		result = 0;
		In >> S;
		flag = S;
		getline(In, temp);
		for (j = 0; j < S; j++)
		{
			getline(In, temp);
			engine[temp] = 0;
		}
		In >> Q;
		getline(In, temp);
		for (j = 0; j < Q; j++)
		{
			getline(In, temp);
			if (engine[temp] == 0)
			{
				engine[temp]++;
				flag--;
			}			
			if ( flag <= 0)
			{
				result++;
				engine.clear();
				engine[temp] = 1; //belong to next switch
				flag = S-1;
			}
			
		}

		Out << "Case #" << i+1 << ": "<<result << endl;
		engine.clear();


	}	
    Out.close();
	In.close();
	return 0;
}

