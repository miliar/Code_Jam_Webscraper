#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
 
using namespace std;
 
typedef vector<bool> VB; typedef vector<double> VD;
typedef vector<int> VI; typedef vector<string> VS;

typedef unsigned int uint;
typedef unsigned long long ull;

int S[501];
int N=0;

int sum(int a)
{
	int res=0;
	for(int i=0;i<N;i++)
		if(a&(1<<i))
			res += S[i];
	return res;
}

int main(void)
{
	string line;
	uint numTests;
	stringstream ss;

	getline(cin, line);
	ss << line;
	ss >> numTests;
	ss.clear();

	for(uint testCase=0; testCase < numTests; testCase++)
	{
		getline(cin, line);
		ss << line;
		ss >> N;
		for(int i=0;i<N;i++)
			ss >> S[i];
		ss.clear();

		N=min(N,32);
		int a=-1;
		int b=-1;

		for(int i=1;i<1<<N;i++) {
			int sa = sum(i);
			for(int j=i+1;j<1<<N;j++) {
				if(sa == sum(j)) {
					a=i;
					b=j;
					break;
				}
			}
			if(a!=-1) break;
		}

		printf("Case #%d:\n", testCase+1);
		if(a!=-1)
		{
			for(int i=0;i<N;i++)
				if(a&(1<<i))
					printf("%d ", S[i]);
			printf("\n");

			for(int i=0;i<N;i++)
				if(b&(1<<i))
					printf("%d ", S[i]);
			printf("\n");
		}
		else
			printf("Impossible\n");
	}

	return 0;
}

