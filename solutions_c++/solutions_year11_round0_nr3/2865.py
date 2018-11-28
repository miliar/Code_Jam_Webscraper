#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <vector>

#define ll long long int
#define clr(a) memset(a, 0, sizeof(a))
#define FOR(a, b) for(int a = 0; a < (b); a++)
#define iter(a) typeof(a.begin())
#define foreach(a, it) for(typeof(a.begin()) it = a.begin(); it != a.end(); it++)

using namespace std;

const long double EPS = 1e-8;
const int INF = 1000000001;

int n;
int a[1001];
bool b[1001];
int ans;

void rek(int k)
{
	if (k == n)
	{
		int s1 = 0;
		int s2 = 0;
		int sum = 0;
		int i1 = 0, i2 = 0;
		FOR(i, n)
			if (b[i])
			{
				s1 ^= a[i];
				sum += a[i];
				i1++;
			}
			else {s2 ^= a[i];i2++;}
		if (i1 == 0 || i2 == 0) return;
		if (s1 == s2) ans = max(ans, sum);
		return;
	}
	b[k] = 0;
	rek(k + 1);
	b[k] = 1;
	rek(k + 1);
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("", "w", stderr);
	int t;
	scanf("%d", &t);
	for(int i0 = 1; i0 <= t; ++i0)
	{
		scanf("%d", &n);
		FOR(i, n)
			scanf("%d", &a[i]);
		ans = -1;
		rek(0);
		printf("Case #%d: ", i0);
		if (ans == -1) printf("NO");
			else printf("%d", ans);
		printf("\n");




	}
	return 0;
}




