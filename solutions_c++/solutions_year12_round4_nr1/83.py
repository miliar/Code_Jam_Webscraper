#include <cstdio>
#include <cstring>
#include <cstdlib>
#define MAXN 10005

struct node
{
	int pos, len, res;
};

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
			scanf("%d %d",&(a[i].pos),&(a[i].len));
			a[i].res = 0;
		}
		int D;
		scanf("%d",&D);
		a[0].res = a[0].pos;
		for (i = 0; i < N; i++)
		{
			if (a[i].res > 0)
			{
				for (j = i+1; j < N; j++)
				{
					if (a[j].pos > (a[i].pos + a[i].res)) break;
					int temp = a[j].pos - a[i].pos;
					if (temp > a[j].len) temp = a[j].len;
					if (temp > a[j].res) a[j].res = temp;
				}
			}
		}
		printf("Case #%d: ",iT+1);
		char flag = 0;
		for (i = 0; i < N; i++)
		{
			if ((a[i].pos + a[i].res) >= D) flag = 1;
		}
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;	
}
