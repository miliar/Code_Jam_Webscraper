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
const int size = 128;
int pr[size][size];
void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int res = 0;
		int n,k;
		cin >> n >> k; 
		for(int i = 0; i < n;++i)
		{
			for(int j = 0;j < k;++j)
				cin >> pr[i][j];
		}
		
		bool is[size][size];
		for(int i = 0;i < n;++i)
			for(int j = 0;j < n;++j)
			{
				is[i][j] = true;
				for(int f = 0;f < k;++f)
					is[i][j] &= pr[i][f] < pr[j][f];
			}
		
		
		int d[1 << 16];
		memset(d,1,sizeof(d));
		for(int i = 0;i < n;++i)
			d[1 << i] = 1;
		d[0] = 0;
		for(int i = 0;i < (1 << n);++i)
		{
			for(int j = 0;j < n;++j)
			{
				if(i == 11 && j == 2) 
					cout << "";
				if(((1 << j) & i) == 0)
				{
					bool f = true;
					for(int k = 0;k < n;++k)
						if(((1 << k) & i) == 1 << k) 
							f &= (is[j][k] || is[k][j]);
					if(f && i > 0)
						d[(1 << j) | i] = min(d[(1 << j) | i],d[i]);
				}
			}	
		}
		int f[1 << 16];
		memset(f,1,sizeof(f));
		for(int i = 0;i < (1 << n);++i)
		{
			for(int b = i;b > 0;b = (b - 1)& i)
			{
				f[i] = min(f[i],d[b] + d[i ^ b]);
				f[i] = min(f[i],f[b] + d[i ^ b]);
				f[i] = min(f[i],d[b] + f[i ^ b]);
				f[i] = min(f[i],f[b] + f[i ^ b]);

			}
			f[i] = min(f[i],d[i]);
		}
		cout << f[(1 << n) - 1] << endl;
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