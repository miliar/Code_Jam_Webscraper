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

int check(int *a, int n)
{
	int res = -1;
	int xor = 0;
	for(int i = 0;i < n;++i)
		xor ^= a[i];
	for(int i = 1;i < (1 << n) - 1;++i)
	{
		int r1 = 0;
		int r2 = 0;
		for(int b = i, j = 0;j < n;++j, b /= 2)
		{
			if(b % 2)
			{
				r1 ^= a[j];
				r2 += a[j];
			}
		}
		if((xor ^ r1) == r1)
		{
			res = max(res, r2);
		}
	}
	return res;
}
const int size = 1000010;
int d[size];
int buff[size];
void SolveForTest()
{
	int n;
	cin >> n;
	//n = 100;
	
	int a[1010];
	int suma = 0;
	int xor = 0;
	for(int i = 0;i < n;++i)
	{
		cin >> a[i];
		//a[i] = rand() % 1000000 + 1;
		suma += a[i];
		xor ^= a[i];
	}
	memset(d, 0, sizeof(d));
	sort(a, a + n);

	d[a[0]] = a[0];
	for(int i = 1;i < n;++i)
	{
		memcpy(buff, d, sizeof(buff) );
		//d[a[i]] = max(d[a[i]],buff[0] + a[i]);
		for(int j = 0;j < size;++j)
		{
			if(buff[j] + a[i] < suma)
			{
				d[j ^ a[i]] = max(d[j ^ a[i]], buff[j] + a[i]);
			}
		}
	}
	int res = -1;
	for(int i = 0;i < size;++i)
	{
		if(d[i] < suma && (xor ^ i) == i)
		{
			res = max(res, d[i]);
		}
	}
	/*int r = check(a,n);
	if(r != res)
	{
		res /= 0;
	}*/
	if(res == -1)
	{
		cout << "NO";
	}
	else cout << res;
}

void Solve()
{
	int T;
	cin >> T;
	for(int t = 0;t < T;++t)
	{
		cout << "Case #" << t + 1 << ": ";
		SolveForTest();
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