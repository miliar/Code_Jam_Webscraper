#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

int n, k, t[40];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	t[0] = 1;
	for(int i = 1; i < 31; i++)
		t[i] = 2*t[i-1];
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		scanf("%d%d", &n, &k);
		if(!((k+1) % t[n]))
			printf("Case #%d: ON\n", c+1);
		else
			printf("Case #%d: OFF\n", c+1);
	}
	return 0;
}