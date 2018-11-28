// BEGIN CUT HERE

#pragma warning( disable : 4786 )
// END CUT HERE
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include<set>

#define SZ 105

typedef struct
{
	double x, y, r;
}Circle;


using namespace std;

double dist(Circle c1, Circle c2)
{
	return(sqrt((c1.x - c2.x) * (c1.x - c2.x) + (c1.y - c2.y) * (c1.y - c2.y)));
}

Circle cir[SZ];

int main()
{
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);

//	freopen("D-large.in", "rt", stdin);
//	freopen("D-large.out", "wt", stdout);
	
	int kase, inp, i, j, k;

	scanf("%d", &inp);

	for(kase = 1; kase <= inp; kase++)
	{
		int n;
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			scanf("%lf %lf %lf", &cir[i].x, &cir[i].y, &cir[i].r);
		}
		double m_rad;
		if(n <= 2)
		{
			m_rad = 0;
			for(i = 0; i < n; i++)
			{
				if(m_rad < cir[i].r)
					m_rad = cir[i].r;
			}
		}
		else
		{
			m_rad = 1e15;
			for(i = 0; i < n - 1; i++)
			{
				for(j = i + 1; j < n; j++)
				{
					double rad = dist(cir[i], cir[j]) + cir[i].r + cir[j].r;
					rad /= 2;
					if(rad < m_rad)
						m_rad = rad;
				}
			}
			for(i = 0; i < n; i++)
			{
				if(m_rad < cir[i].r)
					m_rad = cir[i].r;
			}
		}

		printf("Case #%d: %lf\n", kase, m_rad);
	}
	return 0;
}
