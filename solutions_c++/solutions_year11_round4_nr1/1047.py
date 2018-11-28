#include <vector>
#include <algorithm>
#include <stdio.h>
#include <iostream>

using namespace std;

struct seg
{
	double b;
	double e;
	double w;
};

vector<seg> segs;
double s, r, t, x, tmin, wc;
int ts, n;

bool cmp(seg a, seg b)
{
	return a.w < b.w;
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> ts;
	for(int test = 0; test < ts; test++)
	{
		cin >> x >> s >> r >> t >> n;
		segs.resize(n);
		for(int i = 0; i < n; i++)
			cin >> segs[i].b >> segs[i].e >> segs[i].w;
		sort(segs.begin(), segs.end(), cmp);
		tmin = wc = 0.0;
		for(int i = 0; i < n; i++)
			wc += segs[i].e - segs[i].b;
		if(wc < x)
		{
			x -= wc;
			
			if(t * r >= x)
			{
				tmin += x / r;
				t -= x / r;
			}
			else
			{
				tmin += t + (x - r * t) / s;
				t = 0.0;
			}
		}
		for(int i = 0; i < n; i++)
		{
			if(t > 0)
			{
				if(t >= (segs[i].e - segs[i].b) / (segs[i].w + r))
				{
					t -= (segs[i].e - segs[i].b) / (segs[i].w + r);
					tmin += (segs[i].e - segs[i].b) / (segs[i].w + r);
					continue;
				}
				tmin += t + (segs[i].e - segs[i].b - (segs[i].w + r) * t) / (segs[i].w + s);
				t = 0.0;
			}
			else
				tmin += (segs[i].e - segs[i].b) / (segs[i].w + s);
		}
		printf("Case #%d: %.15lf\n", test + 1, tmin);
	}
	return 0;
}