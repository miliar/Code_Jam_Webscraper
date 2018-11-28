#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

typedef long long ll;

#define MAXN 1001

int tt, n, k, r, e;
int a[MAXN];
ll z[2*MAXN], w[2*MAXN], q;
int d[2*MAXN], p[2*MAXN], l;

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
			a[n+i] = a[i];
			p[i] = 0;
		}
		for (int i = 0; i < n; ++i)
		{
			int j = i, s = a[i];
			while(1)
			{
				if (j+1>=i+n || s+a[j+1]>k) break;
				s += a[++j];
			}
			d[i] = (j+1)%n;
			z[i] = s;
		}
		l = 0;
		for (int i = 0;; i = d[i], ++l)
		{
			if (p[i]>0)
			{
				e = p[i]-1;
				break;
			}
			p[i] = l+1;
			w[l] = (!l?0:w[l-1]) + z[i];
		}
		ll ans = 0;
		if (r>=l) ans += w[l-1], r-=l; else
		{
			cout << "Case #" << t+1 << ": " << w[r-1] << endl;
			continue;
		}
		ll kol = r/(l-e);
		if (kol>0) ans += kol*(!e?w[l-1]:(w[l-1]-w[e-1])), r -= kol*(l-e);
		if (r>0) ans += (!e?w[e+r-1]:w[e+r-1]-w[e-1]);
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}
