#pragma comment (linker, "/STACK:214721677")
#define _CRT_SECURE_NO_WARNINGS
#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <string>
using namespace std;
#define REP(i,n) for (int i=0, _n=(n)-1; i <= _n; ++i)
#define FOR(i,a,b) for (int i=(a), _b=(b); i <= _b; ++i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) ((a).size()))
const double Pi = acos(-1.0);
const double eps = 1e-10;
const double phi = 0.5 + sqrt(1.25);
const int INF = 1000*1000*1000 + 7;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;
typedef bool BOOL;
template < typename T > T sqr (T a) { return (a) * (a); }
template < typename T > T abs (T a) { return (a < 0) ? -(a) : (a); }
template < typename T > T gcd (T a, T b) { return (b) ? gcd(b, a % b) : a; }

#define YES 1
#define NO 0

BOOL dotExists(string theMap[])
{
	BOOL anyDotOccured = NO;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			anyDotOccured |= ('.' == theMap[i][j]);
	return anyDotOccured;
}

BOOL isRow(string theMap[], int row)
{
	BOOL noDots = YES;
	for (int i = 0; i < 4; ++i)
		noDots &= ('.' != theMap[row][i]);
	return noDots;
}

BOOL isCol(string theMap[], int col)
{
	BOOL noDots = YES;
	for (int i = 0; i < 4; ++i)
		noDots &= ('.' != theMap[i][col]);
	return noDots;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int Tests;
	string theMap[10];
	scanf("%d\n", &Tests);
	for (int testNumber = 1; testNumber <= Tests; ++testNumber)
	{
		BOOL printed = NO;
		for (int i = 0; i < 4; ++i)
		{
			getline(cin, theMap[i]);
		}

		for (int index = 0; index < 4; ++index)
		{
			if (!printed)
			if (isRow(theMap, index))
			{
				BOOL xWon = YES;
				BOOL oWon = YES;
				for (int i = 0; i < 4; ++i)
				{
					xWon &= (theMap[index][i] == 'T' || theMap[index][i] == 'X');
					oWon &= (theMap[index][i] == 'T' || theMap[index][i] == 'O');
				}
				if (xWon)
					printf("Case #%d: X won", testNumber);
				else
				if (oWon)
					printf("Case #%d: O won", testNumber);
				printed |= xWon || oWon;
			}
			if (!printed)
			if (isCol(theMap, index))
			{
				BOOL xWon = YES;
				BOOL oWon = YES;
				for (int i = 0; i < 4; ++i)
				{
					xWon &= (theMap[i][index] == 'T' || theMap[i][index] == 'X');
					oWon &= (theMap[i][index] == 'T' || theMap[i][index] == 'O');
				}
				if (xWon)
					printf("Case #%d: X won", testNumber);
				else
				if (oWon)
					printf("Case #%d: O won", testNumber);
				printed |= xWon || oWon;
			}
		}

		if (!printed)
		{
			BOOL xWon = YES;
			BOOL oWon = YES;
			for (int index = 0; index < 4; ++index)
			{
				xWon &= (theMap[index][index] == 'T' || theMap[index][index] == 'X');
				oWon &= (theMap[index][index] == 'T' || theMap[index][index] == 'O');
			}
			if (xWon)
				printf("Case #%d: X won", testNumber);
			else
			if (oWon)
				printf("Case #%d: O won", testNumber);
			printed |= xWon || oWon;
		}

		if (!printed)
		{
			BOOL xWon = YES;
			BOOL oWon = YES;
			for (int index = 0; index < 4; ++index)
			{
				xWon &= (theMap[index][3 - index] == 'T' || theMap[index][3 - index] == 'X');
				oWon &= (theMap[index][3 - index] == 'T' || theMap[index][3 - index] == 'O');
			}
			if (xWon)
				printf("Case #%d: X won", testNumber);
			else
			if (oWon)
				printf("Case #%d: O won", testNumber);
			printed |= xWon || oWon;
		}

		if (!printed)
		{
			if (dotExists(theMap))
				printf("Case #%d: Game has not completed", testNumber);
			else
				printf("Case #%d: Draw", testNumber);
		}

		printf("\n");
		if (testNumber < Tests)
			scanf("\n");
	}
	return EXIT_SUCCESS;
}
