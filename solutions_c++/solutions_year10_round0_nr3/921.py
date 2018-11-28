#include <iostream>
using namespace std;

int n,i,j,k,r,ncase,cases,tmp,now,remain;
int st,c;
int a[10000],next[10000],num[10000],used[10000];
__int64 sum,add;
int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("C-large.out.txt","w",stdout);
	scanf("%d",&cases);
	for (ncase=0; ncase<cases; ncase++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for (i=0; i<n; i++)
		{
			scanf("%d",&a[i]);
			a[i+n] = a[i];
		}
		for (i=0; i<n; i++)
		{
			tmp = a[i]; j = i;
			while (tmp<=k && j<i+n)
			{
				j++;
				tmp = tmp+a[j];
			}
			num[i] = tmp-a[j];
			next[i] = j%n;
		}
		memset(used,0,sizeof(used));
		i = 1; now = 0;
		while (used[now]==0)
		{
			used[now] = i;
			now = next[now];
			i++;
		}
		st = used[now]-1;
		c = i-used[now];
		if (r<=st)
		{
			sum = 0; now = 0;
			for (i=0; i<r; i++)
			{
				sum = sum+num[now];
				now = next[now];
			}
		}
		else
		{
			sum = 0;now = 0;
			for (i=0; i<st; i++)
			{
				sum = sum+num[now];
				now = next[now];
			}
			add = 0;
			for (i=0; i<c; i++)
			{
				add = add+num[now];
				now = next[now];
			}
			sum = sum + (r-st)/c*add;
			for (i=0; i<(r-st)%c; i++)
			{
				sum = sum+num[now];
				now = next[now];
			}
		}
		printf("Case #%d: %I64d\n",ncase+1,sum);
	}
	return 0;
}
