#include "stdafx.h"
#include "fstream"
#include "string"
#include "vector"
#include "set"
#include "iostream"
#include <cstdlib>
#include <iomanip>
#include <algorithm>

using namespace std;

#include <stdio.h>

int find_recycled_num(int a, int b)
{
	char abuf[10];
	_itoa(a, abuf, 10);
	int alen = strlen(abuf);
	if(alen == 1)
		return 0;

	set<long long> pairs;

	int answer = 0;
	for(int i = 1; i < alen; i++) // move "i" digits
	{
		char bbuf[10];
		for(int j = 0; j < alen; j++)
		{
			if(j < i)
				bbuf[j] = abuf[alen - i + j];
			else
				bbuf[j] = abuf[j - i];
		}
		bbuf[alen] = NULL;
		if(bbuf[0] == '0')
			continue;
		int newb = atoi(bbuf);
		if(a < newb && newb <= b)
		{
			if(pairs.find(a + (newb << 22)) == pairs.end())
			{
				pairs.emplace(a + (newb << 22));
				answer++;
				//cout << abuf << " " << bbuf << endl;
			}
		}

	}
	return answer;
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
		int A;
		int B;

		ifs >> A;
		ifs >> B;
		int answer = 0;

		for(int a = A; a < B; a++)
			answer += find_recycled_num(a, B);			
		
		ofs << "Case #"<<i<<": "<<answer<<endl;
	}

	return 0;
}

