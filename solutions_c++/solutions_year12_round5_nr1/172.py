#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#define MAXN 1005

struct node
{
	int t, p, num;
};

using namespace std;

bool IsLess (struct node a, struct node b)
{
	int q1, q2;
	q1 = (100 - b.p) * a.t;
	q2 = (100 - a.p) * b.t;
	if (q1 < q2) return true;
	else if (q1 > q2) return false;
	else
	{
		if (a.num < b.num) return true;
		else return false;
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static struct node a[MAXN];
	for (iT = 0; iT < T; iT++)
	{
		int N;
		scanf("%d",&N);
		int i, j;
		for (i = 0; i < N; i++)
		{
			scanf("%d",&(a[i].t));
			a[i].num = i;
		}
		for (i = 0; i < N; i++)
		{
			scanf("%d",&j);
			j = 100-j;
			a[i].p = j;
		}
		sort(&(a[0]),&(a[N]),IsLess);
		printf("Case #%d:",iT+1);
		for (i = 0; i < N; i++) printf(" %d",a[i].num);
		printf("\n");
	}
	return 0;
}
