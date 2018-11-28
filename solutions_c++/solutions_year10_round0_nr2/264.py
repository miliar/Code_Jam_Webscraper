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

#include "cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
typedef unsigned long long ULL;
typedef cBigNumber cLL;

const int size = 2000;
cLL a[size];
cLL gcd(cLL a,cLL b)
{
	cLL r;
	if(a == 0)
		return b;
	if(b == 0)
		return a;
	if(a == 0 && b == 0)
		return 1;
	for(;;)
	{
		r = a % b;
		if(r == 0)
			return b;
		a = b;
		b = r;
	}
}
cLL abs(cLL &a)
{
	if(a < 0)
		return -a;
	return a;
}
void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int n;
		cin >> n;
		for(int i = 0; i < n;++i)
		{
			cin >> a[i];
		}
		cLL res = 1;
		int ind = 0;
		for(int i = 0; i < n;++i)
		{
			for(int j = 0;j < n;++j)
			{
				if(i != j)
				{
					if(ind == 0)
					{
						res = abs(a[i] - a[j]);
						ind = 1;
					}
					else res = gcd(res,abs(a[i] - a[j]));
				}
			}
		}
		
		res = (-a[0] % res + res) % res;
		cout << res << endl;
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