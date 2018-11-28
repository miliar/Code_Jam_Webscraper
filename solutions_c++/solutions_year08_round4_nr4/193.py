#include<stdio.h>

int perm[1111];
int check[1111];

char a[10000], b[10000];
int n, m;
int ret;

void Go(int Dep)
{
	if(Dep == m)
	{
		int l1, l2;

		for(l1=0;l1<n;l1+=m)
		{
			for(l2=0;l2<m;l2++)
			{
				b[l1 + l2] = a[l1 + perm[l2]];
			}
		}

		int t1 = 1;
		for(l1=1;l1<n;l1++)
		{
			if(b[l1] != b[l1-1]) t1++;
		}
		if(t1 < ret) ret = t1;
	}
	else
	{
		int l1;

		for(l1=0;l1<m;l1++)
		{
			if(check[l1] == 0)
			{
				check[l1] = 1;
				perm[Dep] = l1;
				Go(Dep + 1);
				check[l1] = 0;
			}
		}
	}
}

int main(void)
{
	int T,l0;

	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %s",&m,a);
		for(n=0;a[n];n++);
		ret = n + 1;
		Go(0);
		printf("Case #%d: %d\n",l0,ret);
	}
}