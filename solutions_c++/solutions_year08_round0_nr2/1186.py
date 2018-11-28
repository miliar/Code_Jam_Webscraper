#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define VS vector < string >
#define VI vector < int >
#define PI pair < int, int >
#define X first
#define Y second
#define MP make_pair
#define PB puch_back
#define PIPI pair< int, PI >
#define COS pair< PI, PIPI >

int t, na, nb;

PI dodaj(PI x, int ile)
{
	x.Y += ile;
	while (x.Y >= 60)
	{
		x.Y -= 60;
		x.X++;
	}
	return x;
}

int main()
{
	int nnn;
	scanf("%d", &nnn);
	REP(iii, nnn)
	{
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);
		priority_queue<COS, vector< COS >, greater< COS > > qa, qb;
		REP(i,na)
		{
			char s1[5], s2[5];
			int h1, m1, h2, m2;
			scanf("%s %s", s1, s2);
			h1 = (s1[0]-'0')*10 + (s1[1]-'0');
			m1 = (s1[3]-'0')*10 + (s1[4]-'0');
			h2 = (s2[0]-'0')*10 + (s2[1]-'0');
			m2 = (s2[3]-'0')*10 + (s2[4]-'0');
			qa.push(MP(MP(h1, m1), MP(1, MP(h2, m2))));
		}
		REP(i,nb)
		{
			char s1[5], s2[5];
			int h1, m1, h2, m2;
			scanf("%s %s", s1, s2);
			h1 = (s1[0]-'0')*10 + (s1[1]-'0');
			m1 = (s1[3]-'0')*10 + (s1[4]-'0');
			h2 = (s2[0]-'0')*10 + (s2[1]-'0');
			m2 = (s2[3]-'0')*10 + (s2[4]-'0');
			qb.push(MP(MP(h1, m1), MP(1, MP(h2, m2))));
		}
		int wyna = 0;
		int wynb = 0;
		int a = 0;
		int b = 0;
		int ile = na + nb;
		while (ile)
		{
			COS x = MP(MP(100, 100), MP(100, MP(100, 100)));
			COS y = MP(MP(100, 100), MP(100, MP(100, 100)));
			if (qa.size())
			{
				x = qa.top();
			}
			if (qb.size())
			{
				y = qb.top();
			}
			if (y.X < x.X)
			{
				qb.pop();
				//printf("B: %d %d %d %d %d\n", y.X.X, y.X.Y, y.Y.X, y.Y.Y.X, y.Y.Y.Y);
				if (y.Y.X == 1)
				{
					ile--;
					if (b)
					{
						b--;
					}
					else
					{
						wynb++;
					}
					qa.push(MP(dodaj(y.Y.Y, t), MP(0, MP(-1, -1))));
				}
				else
				{
					b++;
				}
			}
			else
			{
				qa.pop();
				//printf("A: %d %d %d %d %d\n", x.X.X, x.X.Y, x.Y.X, x.Y.Y.X, x.Y.Y.Y);
				if (x.Y.X == 1)
				{
					ile--;
					if (a)
					{
						a--;
					}
					else
					{
						wyna++;
					}
					qb.push(MP(dodaj(x.Y.Y, t), MP(0, MP(-1, -1))));
				}
				else
				{
					a++;
				}
			}
		}
		printf("Case #%d: %d %d\n", iii+1, wyna, wynb);
	}
	return 0;
}


