#include<iostream>
#include<cstdio>

#define INF 1000005

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int n, i, z, zi, xs, s, mi, t;

	scanf("%d", &z);
	for(zi=1;zi<=z;zi++)
	{
		scanf("%d", &n);

		mi = INF;
		s = 0;
		xs = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d", &t);

			xs ^= t;

			s += t;
			mi = min(t, mi);
		}
		if(xs)
			printf("Case #%d: NO\n", zi);
		else
			printf("Case #%d: %d\n", zi, s - mi);
	}
}
