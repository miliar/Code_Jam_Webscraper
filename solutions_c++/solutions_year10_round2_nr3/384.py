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

const int mode = 100003;
const int size = 512;
int d[512][512];
bool use[512][512];
int rec(int i,int j)
{
	if(i == 1 && j == 1)
	{
		return 1;
	}
	if(i == 1)
		return 1;
	if(j == 1)
		return 0;
	if(i == j) return 0;
	if(use[i][j])
		return d[i][j];
	use[i][j] = 1;
	int &res = d[i][j];
	for(int k = 1;k < i;++k)
	{
		res += rec(k,i - 1);
		res %= mode;
	}
	return res; 
}
int che(int n)
{
	int res = 0;
	int np, p[30];
	for(int i = 0;i < (1 << (n - 2));++i)
	{
		int b = i;
		np = 1;
		for(int j = 2;b > 0;b /= 2,++j)
			if(b % 2)
				p[np++] = j;
		p[np++] = n;
		int ind = np - 1;
		int val = np - 1;
		p[0] = 1;
		for(;ind >= 1;--ind)
		{
			if(p[ind] == val)
			{
				val = ind;		
			}
		}
		if(val == 1)
		{
			res++;
			if(res >= mode)
				res -= mode;
		}
	}
	return res;
}
void Solve()
{
	memset(use,0,sizeof(use));
	memset(d,0,sizeof(d));
	
	int pp[26];
	for(int i = 2;i < 26;++i)
		pp[i] = che(i);
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int n;
		cin >> n;
		int res = 0;
		for(int i = 1;i < n;++i)
		{		
			res += rec(i,n);
			res %= mode;
		}
		//cout << res << endl;
		cout << pp[n] << endl;
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