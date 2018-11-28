#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

struct node
{
	bool c;
	bool g;
	int x0;
	int x1;
};


int main()
{
	int N;
	scanf("%d", & N);
	for (int Case = 0; Case < N; Case++)
	{
		int M, V;
		scanf("%d%d", & M, & V);
		
		vector<node> a;

		for (int i = 0; i < (M - 1) / 2; i++)
		{
			int G, C;
			scanf("%d%d", & G, & C);
			node n;
			n.g = G != 0;
			n.c = C != 0;
			a.push_back(n);
		}

		for (int i = (M - 1) / 2; i < M; i++)
		{
			int I;
			scanf("%d", & I);
			node n;
			if (I)
				n.x0 = 999999, n.x1 = 0;
			else
				n.x1 = 999999, n.x0 = 0;
			a.push_back(n);
		}

		for (int i = (M - 1) / 2 - 1; i >= 0; i--)
		{
			node & n = a[i];
			node & l = a[(i + 1) * 2 - 1];
			node & r = a[(i + 1) * 2];
			if (n.g)
			{
				n.x0 = min(l.x0, r.x0);
				if (n.c)
					n.x1 = min(l.x1 + r.x1, min(l.x1, r.x1) + 1);
				else
					n.x1 = l.x1 + r.x1;
			}
			else
			{
				n.x1 = min(l.x1, r.x1);
				if (n.c)
					n.x0 = min(l.x0 + r.x0, min(l.x0, r.x0) + 1);
				else
					n.x0 = l.x0 + r.x0;
			}
		}

		int R = V ? a[0].x1 : a[0].x0;
		if (R > M)
			printf("Case #%d: IMPOSSIBLE\n", Case + 1);
		else
			printf("Case #%d: %d\n", Case + 1, R);
	}
	return 0;
}
