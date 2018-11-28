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

const int size = 300;
int n;
pair<double,LL> v[size], buff[size];
void SolveForTest()
{
	int n; 
	cin >> n;
	LL d;
	cin >> d;
	for(int i = 0;i < n;++i)
	{
		cin >> v[i].first >> v[i].second;
	}
	sort(v, v + n);
	for(int i = 0;i < n;++i)
		buff[i] = v[i];

	double s = 0; 
	double e = 1e20;
	double res = 0;
	for(int i = 0;i < 256;++i)
	{

		double t = (s + e) / 2;
		//t = 2;
		t /= d;
		for(int i = 0;i < n;++i)
		{
			v[i] = buff[i];
			v[i].first /= d;
		}
		double lim = v[0].first - t - 1;
		
		bool is = true;	
		for(int i = 0;i < n;++i)
		{
			double L = v[i].first - t;
			double R = v[i].first + t;
			if(floor(R - L + 1) + 1e-9 >= v[i].second && lim <= R && floor(R - lim) + 1e-9 >= v[i].second)
			{
				lim = max(lim + v[i].second, v[i].first - t + v[i].second - 1);
			}
			else
			{
				is = false;
				break;
			}
		}
		if(is)
		{
			res = (s + e) / 2;
			e = res;
		}
		else s = (s + e) / 2;
	}
	printf("%.10lf", res);
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