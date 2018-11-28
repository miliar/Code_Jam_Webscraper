#include<cstdio>
#include<iostream>
#include<algorithm>
#define Max 10005

#define MP make_pair
#define F first
#define S second

using namespace std;

pair<int, double> seg[Max];
int main()
{
	int z, zi, x, s, r, n, t, i, a, b, l;
	double T, ans, dt;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		T = t;

		for(i=0;i<n;i++)
		{
			scanf("%d %d %d", &a, &b, &t);
			seg[i].F = t + s;

			l = b - a;

			seg[i].S = l;
			x -= l;
		}
		seg[n].F = s;
		seg[n].S = x;
		n++;

		sort(seg, seg+n);

		r -= s;
		ans = 0.0;
		for(i=0;i<n;i++)
		{
//			cout<<seg[i].F<<" "<<seg[i].S<<"\n";

			dt = min(seg[i].S/(seg[i].F+r), T);

			seg[i].S -= dt * r;
			T -= dt;

			//cout<<dt<<" "<<T<<"\n";

			ans += seg[i].S / seg[i].F;
		}
		printf("Case #%d: %.8lf\n", zi, ans);
	}
}
