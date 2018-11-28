#include <stdio.h>
#include <iostream>

using namespace std;

const int N = 1000;

class Walkway
{
	public:
		int b, e, w;
		bool operator<(const Walkway obj) const
		{
			return w<obj.w;
		}
};

int main()
{
	int t;
	int x, s, r, irt, n;
	int wl, rl;
	double dwl, drl;
	double rt, ans;
	Walkway w[N];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans = 0;
		scanf("%d%d%d%d%d", &x, &s, &r, &irt, &n);
		for (int j=0;j<n;j++)
			scanf("%d%d%d", &w[j].b, &w[j].e, &w[j].w);
		wl = w[0].b;
		for (int j=1;j<n;j++)
			wl += w[j].b - w[j-1].e;
		wl += x-w[n-1].e;
		sort(w, w+n);
		rl = (irt*r)<?wl;
		wl -= rl;
		ans += double(rl)/r+double(wl)/s;
		rt = irt-double(rl)/r;
		for (int j=0;j<n;j++)
		{
			dwl = w[j].e-w[j].b;
			drl = (rt*(r+w[j].w))<?dwl;
			dwl -= drl;
			ans += drl/(r+w[j].w)+dwl/(s+w[j].w);
			rt -= drl/(r+w[j].w);
		}
		printf("Case #%d: %.10lf\n", i, ans);
	}
	return 0;
}
