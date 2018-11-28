#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int tim[2][2][101];
int u[2][101];

int d;
int rei[2];
int freeaa;
int freebb;
int tot1, tot2;
int freee[2];

void doit(int z, int t0)
{
	int mint = INT_MAX;
	int mini = -1;

	for (int i = 0; i < rei[z]; i++)
	{
		if (u[z][i] == 0 && tim[z][0][i] >= t0 && tim[z][0][i] < mint)
		{
			mint = tim[z][0][i];
			mini = i;
		}
	}

	if (mini != -1)
	{
		u[z][mini] = 1;
		freee[z]--;
		doit(1-z, tim[z][1][mini]+d);
	}
}

int best_start()
{
	int mint = INT_MAX;
	int best = -1;

	for (int z = 0; z < 2; z++)
	{
		for (int i = 0; i < rei[z]; i++)
		{
			if (u[z][i] == 0 && tim[z][0][i] < mint)
			{
				mint = tim[z][0][i];
				best = z;
			}
		}
	}
	return best;
}



int readtime()
{
	char c1,c2,c3,c4,c5;
	scanf("%c%c%c%c%c", &c1,&c2,&c3,&c4,&c5);
	return ((c1-'0')*10+(c2-'0'))*60 + (c4-'0')*10+(c5-'0');
}

int main()
{
	freopen("c:\\b.txt", "r", stdin);
	freopen("c:\\b_out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int te = 1; te <= t; te++)
	{
		scanf("%d %d %d\n", &d, &rei[0], &rei[1]);

		for (int i = 0; i < rei[0]; i++)
		{
			tim[0][0][i] = readtime();
			char space;
			scanf("%c", &space);
			tim[0][1][i] = readtime();
			scanf("\n");
		}

		for (int i = 0; i < rei[1]; i++)
		{
			tim[1][0][i] = readtime();
			char space;
			scanf("%c", &space);
			tim[1][1][i] = readtime();
			scanf("\n");
		}

		memset(u,0,sizeof(u));


		freee[0] = rei[0];
		freee[1] = rei[1];
		tot1 = 0;
		tot2 = 0;

		while (freee[0]+freee[1] > 0)
		{

			if (best_start() == 0)
			{
				tot1++;
				doit(0, 0);
			}
			else
			{
				tot2++;
				doit(1, 0);
			}
		}

		printf("Case #%d: %d %d\n", te, tot1, tot2);
	}




	return 0;
}
