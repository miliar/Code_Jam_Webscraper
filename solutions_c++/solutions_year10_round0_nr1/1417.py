#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <limits.h>

using namespace std;


bool check(long long n, long long k)
{
	long long q = (1LL << n);
	return ((k + 1) % q == 0);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n, k;
		cin >> n >> k;
		printf("Case #%d: %s\n", i + 1, check(n, k) ? "ON" : "OFF");
	}
	return 0;
}