#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())

int n, k;

bool can(int n, int k)
{
	return ((((1 << n) - 1) & k) == ((1 << n) - 1)) ? true : false; 
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cin >> n >> k;
		printf("Case #%d: %s\n", test + 1, can(n, k) ? "ON" : "OFF");
	}

	return 0;
}