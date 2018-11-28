// Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "string"
#include "vector"
#include "iostream"
#include <iomanip>
#include <algorithm>

using namespace std;

#include <stdio.h>


int get_max(int total, bool isStrange) {
	if(total > 27)
		return 10;
	if(total < 2)
		return total;

	int mod = total%3;
	int div = total/3;


	int notStrange = mod ? div + 1 : div;
	if(!isStrange)
	{
		return notStrange;
	}
	else
	{
		return mod == 1 ? notStrange : notStrange + 1;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{

	if(argc < 2)
		return 1;
	int num;
	ifstream ifs(argv[1]);
	ifs >> num;

	ofstream ofs("output.txt");	

	for(int i = 1; i <= num; i++)
	{
		int N;
		int S;
		int p;

		ifs >> N;
		ifs >> S;
		ifs >> p;

		vector<int> t(N);
		int answer = 0;
		
		for(unsigned j = 0; j < N; j++)
		{
			ifs >> t[j];

			int max_usual = get_max(t[j], false);
			int max_strange = get_max(t[j], true);

			if(max_usual >= p)
				answer++;
			else if(S && max_strange >= p)
			{
				answer++;
				S--;
			}
		}
		ofs << "Case #"<<i<<": "<<answer<<endl;
	}

	return 0;
}

