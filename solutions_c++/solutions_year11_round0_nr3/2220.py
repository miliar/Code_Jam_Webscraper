#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define INF 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define NMax 1024

int N, x;

int main()
{
	int T, test, i, m;
	int sumxor, sum;
	
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	scanf("%d", &T);
	for (test = 1; test <= T; ++test)
	{
		scanf("%d", &N);
		sumxor = 0;
		sum = 0;
		m = INF;
		for (i = 1; i <= N; ++i)
		{
			scanf("%d", &x);
			sumxor ^= x;
			sum += x;
			m = minim(m, x);
		}
		if (sumxor)
			printf("Case #%d: NO\n", test);
		else
			printf("Case #%d: %d\n", test, sum-m);
	}
	
	return 0;
}
