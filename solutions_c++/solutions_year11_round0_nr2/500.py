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


void SolveForTest()
{
	int c;
	cin >> c;
	vector<string> comb(c);
	for(int i = 0;i < c;++i)
	{
		cin >> comb[i];
	}
	int d;
	cin >> d;
	vector<string> oposed(d);
	for(int i = 0;i < d;++i)
		cin >> oposed[i];
	int n;
	cin >> n;

	string str;
	cin >> str;
	string res;
	for(int i = 0;i < str.size();++i)
	{
		res += str[i];
		if(res.size() > 1)
		{
			char ch1 = res[res.size() - 1];
			char ch2 = res[res.size() - 2];
			bool is = false ;
			for(int i = 0;i < c;++i)
			{
				if((ch1 == comb[i][0] && ch2 == comb[i][1]) ||
					(ch2 == comb[i][0] && ch1 == comb[i][1]))
				{
					res = res.substr(0, res.size() - 2);
					res += comb[i][2];
					is = true;
					break;
				}
			}
			if(is)
			{
				continue;
			}
		}
		for(int k = 0;k < d;++k)
		{
			
			for(int j = 0;j < res.size() - 1;++j)
			{
				char ch1 = res[j];
				char ch2 = res[res.size() - 1];
				if((ch1 == oposed[k][0] && ch2 == oposed[k][1]) ||
					(ch2 == oposed[k][0] && ch1 == oposed[k][1]))
				{
					res = "";
					break;
				}
			}
			if(res.size() == 0) break;
		}
	}
	cout << "[";
	for(int i = 0;i < res.size();++i)
	{
		if(i > 0)
			cout << ", ";
		cout << res[i];
	}
	cout << "]";
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