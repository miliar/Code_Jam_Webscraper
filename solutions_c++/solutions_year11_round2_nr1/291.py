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

const int size = 200;
char d[size][size];
int n;
void SolveForTest()
{
	cin >> n; 
	for(int i = 0;i < n;++i)
		for(int j = 0;j < n;++j)
		{
			cin >> d[i][j];
		}
	double WPr[size], WPc[size];
	for(int i = 0;i < n;++i)
	{
		WPr[i] = WPc[i] = 0;
		for(int j = 0;j < n;++j)
		{
			WPr[i] += d[i][j] != '.';
			WPc[i] += d[i][j] == '1';
		}
	}
	double OWP[size];
	for(int i = 0;i < n;++i)
	{
		OWP[i] = 0;
		int count = 0;
		for(int j = 0;j < n;++j)
		{
			double r = WPr[j];
			double c = WPc[j];
			if(i == j) continue;
			if(d[j][i] != '.')
			{
				OWP[i] += (c - (d[j][i] == '1')) / (r - 1);
				++count;
			}
		}
		OWP[i] /= count;
	}
	double OOWP[size];
	for(int i = 0;i < n;++i)
	{
		OOWP[i] = 0;
		int count = 0;
		for(int j = 0;j < n;++j)
		{
			if(d[i][j] != '.')
			OOWP[i] += OWP[j], ++count;
		}
		OOWP[i] = (OOWP[i]) / count;
	}
	printf("\n");
	for(int i = 0;i < n;++i)
	{
		double res = 0.25 * WPc[i]/WPr[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]; 
		printf("%.10lf", res);
		if(i != n - 1)
			printf("\n");
	}

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