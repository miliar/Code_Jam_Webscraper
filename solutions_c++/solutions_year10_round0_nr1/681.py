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
typedef unsigned long long ULL;
const int size = 3000;
int g[size + 1];
LL suma[size];
void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		LL n;
		LL k;
		cin >> n >> k;
		LL res = (k % (1LL << (n)));
		bool is_res = true;
		if(res == 0)
			is_res = false;
		else
		{
			
			for(int j = 0;j < n;res /= 2, ++j)
				is_res &= res % 2 == 1;
		}
		if(is_res)
			cout << "ON" << endl;
		else cout << "OFF" << endl; 
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