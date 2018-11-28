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

#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
typedef unsigned long long ULL;
typedef cBigNumber cLL;


void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int n,k,b,t;
		cin >> n >> k >> b >> t;
		vector<int> x(n), v(n);

		for(int i = 0;i < n;++i)
		{
			cin >> x[i];
		}
		for(int i = 0;i < n;++i)
			cin >> v[i];
		int res = 0;
		vector<bool> use(n,1);
		int num = 0;
		for(int i = n - 1;i >= 0;--i)
		{
			if(b - x[i] <= (ULL) t * v[i] && num < k)
			{
				++num;
				use[i] = 0;
				for(int j = i + 1; j < n;++j)
					res += use[j];
			}
		}
		if(num >= k)
			cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
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