#include <vector>
#include <math.h>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;

struct tri
{
	int x, y, r;
};

double check(tri t1, tri t2, tri t3)
{
	double r = (double)t1.r;
	double r2 = sqrt( (double)(t2.x-t3.x)*(t2.x-t3.x) + (t2.y-t3.y)*(t2.y-t3.y) );
	r2 += (double)t2.r + (double)t3.r;

	if (r2 > r) return r2;
	return r;
}

int main()
{
	int i,l,k,j;
	int T, N;
	int a,b,d;
	double r,rt;

	scanf("%d", &T);
	for (k=0; k<T; k++)
	{
		vector <tri> v;

		scanf("%d", &N);
		for (i=0; i<N; i++)
		{
			scanf("%d %d %d", &a, &b, &d);
			tri nt = {a, b, d};
			v.push_back(nt);
		}

		if (v.size() == 1)
		{
			r = (double)v[0].r;
		}

		if (v.size() == 2)
		{
			if (v[0].r > v[1].r) r = (double)v[0].r;
			else r = (double)v[1].r;
		}

		if (v.size() == 3)
		{
			r = 10000000.0;
			rt = check(v[0], v[1], v[2]);
			if (rt < r) r = rt;
			rt = check(v[1], v[0], v[2]);
			if (rt < r) r = rt;
			rt = check(v[2], v[0], v[1]);
			if (rt < r) r = rt;
			r /= 2.0;
		}
		
		printf("Case #%d: %lf\n", k+1, r);

	}

	char c;
	scanf("%c", &c);
	return 0;
}
