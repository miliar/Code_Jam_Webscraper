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
		int R;
		int k;
		int N;
		cin >> R >> k >> N;
		for(int i = 0;i < N;++i)
		{
			scanf("%d",&g[i + 1]);
			g[i + N + 1] = g[i + 1];
		}
		suma[0] = 0;
		for(int i = 1;i <= 2 * N;++i)
			suma[i] = suma[i - 1] + g[i];
		int ind = 0;
		LL res = 0;
		for(int i = 0;i < R;++i)
		{
			int s = ind;
			int e = ind + N;
			int r = ind;
			while(s <= e)
			{
				int mid = (s + e) / 2;
				LL val = suma[mid] - suma[ind];
				if(val > k)
				{
					e = mid - 1;
				}
				else if(val <= k)
				{
					s = mid + 1;
					r = mid;
				}
			}
			res += suma[r] - suma[ind];
			ind = r; 
			if(ind != 0)
			{
				ind = ((ind - 1) % N + 1);
			}
		}
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