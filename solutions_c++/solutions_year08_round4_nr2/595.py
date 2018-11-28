#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

struct St
{
	int a;
	int c;
	St()
	{
		a = -1;
	}
};

int N,M;

St calc(int a, int x, int y)
{
	St p1;
	if (a == 0)
	{
		p1.a = x;
		p1.c = M;
	}
	for (int bx = 0; bx <= N; bx++)
	{
		if (bx == x)
			continue;
		if (a % (bx-x) == 0)
		{
			int cy = a/(bx-x)+y;
			if (cy >= 0 && cy <= M)
			{
				p1.a = bx;
				p1.c = cy;
				return p1;
			}
		}
	}
	return p1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		bool isRes = false;
		int A;
		scanf("%d%d%d", &N, &M, &A);

		int mm = N*M-A;
		int Ax,Ay, Bx,By, Cx,Cy;
		for (int i=0; i<=mm && !isRes; i++)
		{
			for (int x=0; x<=N && !isRes; x++)
			{
				for (int y=0; y<=M && !isRes; y++)
				{
					St p1 = calc(i,x,y);
					if (p1.a == -1)
						continue;
					St p2 = calc(i+A,x,y);
					if (p2.a == -1)
						continue;
					isRes = true;
					Ax = x;
					Ay = y;
					Bx = p1.a;
					Cy = p1.c;
					Cx = p2.a;
					By = p2.c;

				}
			}
		}

		if (isRes)
		{
			printf("Case #%d: %d %d %d %d %d %d\n",tt, Ax,Ay, Bx,By, Cx,Cy);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
	return 0;
}