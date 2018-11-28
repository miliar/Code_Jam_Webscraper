#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

struct it
{
	int x,y;
	it(int xx=0, int yy=0)
	{
		x=xx,y=yy;
	}
	bool friend operator < (it a, it b)
	{
		return a.y<b.y || a.y==b.y && a.x>b.x;
	}
};

int nn,n,m,k;

int ra,rb,fa,fb;
vector<it> v;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d\n",&nn);
	for (int ii=1; ii<=nn; ++ii)
	{
		scanf("%d\n%d %d\n",&k,&n,&m);

		v.clear();

		for (int i=1; i<=n; ++i)
		{
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			v.push_back(it(0, h1*60+m1));
			v.push_back(it(2, h2*60+m2+k));
		}

		for (int i=1; i<=m; ++i)
		{
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			v.push_back(it(1, h1*60+m1));
			v.push_back(it(3, h2*60+m2+k));
		}

		sort(v.begin(), v.end());

		ra=rb=fa=fb=0;

		for (vector<it>::iterator i = v.begin();
			 i != v.end();
			 ++i)
		{
			switch (i->x)
			{
			case 0:
				if (ra>0)
					--ra;
				else
					++fa;
				break;
			case 2:
				++rb;
				break;
			case 1:
				if (rb>0)
					--rb;
				else
					++fb;
				break;
			case 3:
				++ra;
				break;
			}
		}

		printf("Case #%d: %d %d\n", ii, fa, fb);
	}
	return 0;
}
