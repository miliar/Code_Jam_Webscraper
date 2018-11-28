#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std; 

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;


int fn[51][51];
int f[51][51];
int n, k;

bool TestF(int w)
{
	int cnt = 0;
	for (int i = 0; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n; j++)
		{
			if (fn[i][j] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	cnt = 0;
	for (int i = 0; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n; j++)
		{
			if (fn[j][i] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	cnt = 0;
	for (int i = 0; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (fn[i + j][j] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	cnt = 0;
	for (int i = 1; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (fn[j][i + j] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	cnt = 0;
	//--------------------------------//
	for (int i = 0; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (fn[i + j][n - 1 - j] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	cnt = 0;
	for (int i = 1; i < n; i++, cnt = 0)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (fn[j][n - 1 - (i + j)] == w) cnt++;
			else cnt = 0;
			if (cnt == k)
				return true;
		}
	}
	return false;
}

void Gravity()
{
	for (int j = 0; j < n; j++)
	{
		int curPos = n - 1;
		for (int i = n - 1; i >= 0; i--)
		{
			if (fn[i][j] > 0)
			{
				fn[curPos][j] = fn[i][j];
				curPos--;
			}
		}
		for (int i = 0; i <= curPos; i++)
			fn[i][j] = 0;
	}
}

void PrintArray(int f[51][51])
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			char c = '.';
			if (f[i][j] == 0)
				c = '.';
			else if (f[i][j] == 1)
				c = 'R';
			else 
				c = 'B';
			printf("%c", c);
		}
		printf("\n");
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++)
	{
		
		scanf("%d%d", &n, &k);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				char c;
				scanf("%c", &c);
				if (c == '.')
					f[i][j] = 0;
				else if (c == 'R')
					f[i][j] = 1;
				else if (c == 'B')
					f[i][j] = 2;
				else
				{
					j--;
					continue;
				}
			}
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				fn[j][n - i - 1] = f[i][j];
		Gravity();
		bool testBlue = TestF(2), testRed = TestF(1);
		printf("Case #%d: ",tc + 1);
		if (testBlue && testRed)
			puts("Both");
		else if (testBlue)
			puts("Blue");
		else if (testRed)
			puts("Red");
		else 
			puts("Neither");

	}		
	return 0;
}