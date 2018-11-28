#define ONLINE_JUDGE
//#define GenerateTest

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <hash_set>
#include <hash_map>

//#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;

void Solve()
{
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> word(D);
	for(int i = 0;i < D;++i)
	{
		cin >> word[i];
	}
	for(int i = 0;i < N;++i)
	{
		string patt;
		cin >> patt;
		vector<vector<bool> > d(L,vector<bool>(26,0));
		int ind = 0;
		for(int i = 0;i < patt.size();)
		{
			if(patt[i] == '(')
			{
				for(++i;patt[i] != ')';++i)
					d[ind][patt[i] - 'a'] = 1;
				++ind;
				++i;
			}
			else
			{
				d[ind++][patt[i] - 'a'] = 1;
				++i;
			}
		}
		int res = 0;
		for(int j = 0;j < D;++j)
		{
			bool is = true;
			for(int k = 0;k < L;++k)
				is &= d[k][word[j][k] - 'a'];
			res += is;
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}

int main()
{
#ifdef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	
#ifdef GenerateTest
	
	freopen("output.txt", "wt", stdout);

#endif

	clock_t start = clock();
#endif

	Solve();	

#ifndef ONLINE_JUDGE 
	clock_t end = clock();
	cout <<"\n\nTime: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
#endif
	return 0;
}