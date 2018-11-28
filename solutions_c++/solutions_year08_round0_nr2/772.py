#include<iostream>
#include<algorithm>

using namespace std;

struct  Trip
{
	int st, rt;
};

bool cmp(Trip t1, Trip t2)
{
	if (t1.st < t2.st) return 1;
	else if (t1.st == t2.st)
		if (t1.rt < t2.rt) return 1;
	return 0;
}

Trip a[110], b[110];
bool flaga[110], flagb[110];

int main()
{
	//freopen("a.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int n;
	int na, nb, t;
	scanf("%d", &n);
	int caseID = 1;
	while (caseID <= n)
	{
		memset(flaga, 0, sizeof(flaga));
		memset(flagb, 0, sizeof(flagb));
		printf("Case #%d: ", caseID++);
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);
		int h, m;
		int i, j, k;
		for (i = 0; i < na; i++)
		{
			scanf("%d:%d", &h, &m);
			a[i].st = h * 60 + m;
			scanf("%d:%d", &h, &m);
			a[i].rt = h * 60 + m;
			a[i].rt += t;
		}
		for (i = 0; i < nb; i++)
		{
			scanf("%d:%d", &h, &m);
			b[i].st = h * 60 + m;
			scanf("%d:%d", &h, &m);
			b[i].rt = h * 60 + m;
			b[i].rt += t;
		}
		sort(a, a + na, cmp);
		sort(b, b + nb, cmp);
		int numa = 0, numb = 0, curt;
		while (1)
		{
			i = j = 0;
			while (flaga[i]) i++;
			while (flagb[j]) j++;
			//printf("%d %d\n", i, j);
			if (i == na || j == nb) break;
			if (a[i].st <= b[j].st)
			{
				//printf("a:%d %d\n", i, j);
				numa++;
				flaga[i] = 1;
				curt = a[i].rt;
				while (1)
				{
					for (k = j; k < nb; k++)
						if (!flagb[k] && curt <= b[k].st) break;
					if (k == nb) break;
					flagb[k] = 1;
					curt = b[k].rt;
					for (k = i; k < na; k++)
						if (!flaga[k] && curt <= a[k].st) break;
					if (k == na) break;
					flaga[k] = 1;
					curt = a[k].rt;
				}
			}
			else
			{
				//printf("b:%d %d\n", i, j);
				numb++;
				flagb[j] = 1;
				curt = b[j].rt;
				while (1)
				{
					for (k = i; k < na; k++)
						if (!flaga[k] && curt <= a[k].st) break;
					if (k == na) break;
					flaga[k] = 1;
					curt = a[k].rt;
					for (k = j; k < nb; k++)
						if (!flagb[k] && curt <= b[k].st) break;
					if (k == nb) break;
					flagb[k] = 1;
					curt = b[k].rt;
				}
			}
		}
		for (i = 0; i < na; i++)
			if (!flaga[i]) numa++;
		for (i = 0; i < nb; i++)
			if (!flagb[i]) numb++;
		printf("%d %d\n", numa, numb);
	}
	return 0;
}