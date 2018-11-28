#define ONLINE_JUDGE

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <numeric>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>

#include <assert.h>
//#include "BigInteger\cbignum.h"
using namespace std;

#pragma comment(linker, "/STACK:264777216")

typedef long long LL;
typedef long long cBigNumber;
typedef unsigned int uint;
typedef unsigned long long ULL;

void Solve()
{
	int T;
	cin >> T;
	for(int t = 0;t < T;++t)
	{
		cout << "Case #" << t + 1 << ": ";

		int n;
		cin >> n;
		
		int so = 1;
		int sb = 1;
		const int size = 200;
		int d[size] = {0};
		char s[size];
		int k[size];
		k[0] = 1;
		s[0] = 3;
		d[0] = 0;
		for(int i = 1;i <= n;++i)
		{
			char ch;
			int _k;
			cin >> ch >> _k;
			if(ch == 'O')
				s[i] = 0;
			else s[i] = 1;
			k[i] = _k;
			d[i] = d[i - 1] + 1;
			bool is = true;
			for(int j = i - 1;j >= 1;--j)
			{
				if(s[j] == s[i])
				{
					d[i] = max(d[i],d[j] + abs(k[i] - k[j]) + 1);
					is = false;
					break;
				}
			}
			if(is)
			{
				d[i] = max(d[i], d[0] + abs(k[i] - k[0]) + 1);
			}
		}
		cout << d[n]; 

		cout << endl;
	}
}

#ifndef ONLINE_JUDGE
#include <ctime>
#endif

//#define GenerateTest

int main()
{

#ifdef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
#ifdef GenerateTest

	for(int t = 0;;++t){
		freopen("input.txt", "wt", stdout);

		int n = 10;
		cout << n << endl;
		for(int i = 0;i < n;++i)
			cout << (char)(rand() % 10 + 'a');

		fflush(stdout);

		cin.clear();
		cout.clear();

		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
		Solve();
		cin.clear();
		cout.clear();

	}

	return 0;
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