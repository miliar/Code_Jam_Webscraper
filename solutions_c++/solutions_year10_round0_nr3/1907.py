#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

#define ll long long

int g[1005];
int use[1005];
ll sum[1005];

#define qu(i) ( (i>n) ? (i-n) : (i) )

ll solve()
{
	memset(&use[0], 0, sizeof(use));
	memset(&sum[0], 0, sizeof(sum));

	int r, k, n; scanf("%d%d%d", &r, &k, &n);
	for (int i=1; i<=n; ++i) scanf("%d", &g[i]);
	
	int i=0; int s=1;
	while (!use[s]) {
		i++;
		use[s] = i;
		ll w = 0;
		for (int j=s; j<s+n; ++j) {
			if (w+g[qu(j)]<=k) w+=g[qu(j)];
			else {s=qu(j); break;}
		}
		sum[i] = sum[i-1] + w;
		if (i==r) return sum[i];
	}

	ll res = sum[i]; r-=i;
	int st=use[s], en=i; int ln = en-st+1;
	res += (sum[en]-sum[st-1]) * (r/ln) + (sum[st+(r%ln)-1] -sum[st-1]);
	return res;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t; scanf("%d", &t);
	for (int i=1; i<=t; ++i)
		printf("Case #%d: %lld\n", i, solve());
	return 0;
}
