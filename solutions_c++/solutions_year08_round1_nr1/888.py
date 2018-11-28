#include <stdio.h>
#include <tchar.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <conio.h>
#include <algorithm>
#include <map>
#include <queue>
#include <limits>
#include <iterator>
using namespace std;

int main()
{
	ifstream In("A.in");
	ofstream Out("A-large.out");
	unsigned int N = 0;
	In >> N;
	for(unsigned int i = 0; i < N; ++i)
	{
		int Number = 0;
		In >> Number;
		vector<int> v1;
		for(unsigned int j = 0; j < Number; ++j)
		{
			int t;
			In >> t;
			v1.push_back(t);
		}
		vector<int> v2;
		for(unsigned int j = 0; j < Number; ++j)
		{
			int t;
			In >> t;
			v2.push_back(t);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		vector<int> v3;
		for(unsigned int j = 0; j < v1.size(); ++j)
		{
			int t = v1[j]*v2[v1.size()-j-1];
			v3.push_back(t);
		}
		int result = 0;
		for(unsigned int j = 0; j < v3.size(); ++j)
		{
			result += v3[j];
		}
		if(i != 0)
			Out << endl;
		Out << "Case #" << i + 1 << ": " << result;
	}
}