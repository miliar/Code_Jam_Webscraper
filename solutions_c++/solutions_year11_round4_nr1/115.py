#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <bitset>
#include <queue>

using namespace std;

int X, S, t, R, n;
int B[2000], E[2000], w[2000];

int num[2000];

bool comp(int x, int y)
{
	return w[x] < w[y];
}

void solve(int test)
{
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &n);
	for (int i = 1; i <= n; i ++)
		scanf("%d%d%d", &B[i], &E[i], &w[i]), num[i] = i;
	sort(num + 1, num + n + 1, comp);

	double best = 1e9;
	double cur = 0.0;
	double have = t;
	double len = X;
	for (int i = 1; i <= n; i ++)
		len -= (double)(E[num[i]] - B[num[i]]);
	double q = min(have, len / (double)(R));
	cur += q;
	cur += (len - q * (double)(R)) / (double)(S);
	have -= q;
	for (int i = 1; i <= n; i ++)
	{
		len -= (double)(E[num[i]] - B[num[i]]);
		double q = (double)(E[num[i]] - B[num[i]]) / (double)(R + w[num[i]]);
		double p = min(have, q);
		have -= p;
		cur += p;
		cur += ((double)(E[num[i]] - B[num[i]]) - p * (double)(R + w[num[i]])) / (double)(S + w[num[i]]);
	}
	
	printf("Case #%d: %.10lf\n", test, cur);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d\n", &test);
	for (int i = 1; i <= test; i ++)
		solve(i);

	return 0;
}