#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXT = 104;
const int INF = 1000000;

struct tline
{
	int dt;
	int at;
	int ind;
};

int brt;
int na, nb;
int t;
tline t1[MAXT];
tline t2[MAXT];
int nextConn1[MAXT];
int nextConn2[MAXT];
int numTr1[MAXT];
int numTr2[MAXT];

void findConnections()
{
	int ind;

	for(int i = 0; i < na; i++)
	{
		ind = 0;
		while (ind < nb && t1[i].at + t > t2[ind].dt)
			ind++;

		nextConn1[i] = ind;
	}

	for(int i = 0; i < nb; i++)
	{
		ind = 0;
		while (ind < na && t2[i].at + t > t1[ind].dt)
			ind++;

		nextConn2[i] = ind;
	}
}

bool cmp(tline e1, tline e2)
{
	if (e1.dt > e2.dt)
		return false;
	else if (e1.dt < e2.dt)
		return true;
	else if (e1.at > e2.at)
		return false;
	else if (e1.at < e2.at)
		return true;
	else if(e1.ind > e2.ind)
		return false;
	else
		return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("task2.out", "w", stdout);

	int h1,h2;
	int m1,m2;
	int ans1;
	int ans2 ;

	scanf("%d", &brt);

	for(int gi = 1; gi <= brt; gi++)
	{
		ans1 = ans2 = 0;

		scanf("%d", &t);
		scanf("%d %d", &na, &nb);

		memset(numTr1, 0, sizeof(numTr1));
		memset(numTr2, 0, sizeof(numTr2));

		for(int i = 0; i < na; i++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			t1[i].dt = h1*60 + m1;
			t1[i].at = h2*60 + m2;
			t1[i].ind = i;
		}

		for(int i = 0; i < nb; i++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			t2[i].dt = h1*60 + m1;
			t2[i].at = h2*60 + m2;
			t2[i].ind = i;
		}
		
		sort(t1, t1+na, cmp);
		sort(t2, t2+nb, cmp);

		int ia = 0;
		int ib = 0;

		findConnections();

		t1[na].dt = INF;
		t2[nb].dt = INF;

		while (ia < na || ib < nb)
		{
			if (t1[ia].dt < t2[ib].dt)
			{
				// we start from left side
				if (numTr1[ia] == 0)
				{
					ans1++;
				}
				else
				{
					numTr1[ia+1] += numTr1[ia] - 1;
				}

				numTr2[nextConn1[ia]]++;
				ia++;
			}
			else
			{
				// we start from right side
				if (numTr2[ib] == 0)
				{
					ans2++;
				}
				else
				{
					numTr2[ib+1] += numTr2[ib] - 1;
				}

				numTr1[nextConn2[ib]]++;
				ib++;
			}
		}

		printf("Case #%d: %d %d\n", gi, ans1, ans2);
	}

	return 0;
}
