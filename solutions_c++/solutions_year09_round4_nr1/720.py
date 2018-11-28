#include <stdio.h>
#include <string.h>
typedef struct Line
{
	char a[41];
}Line;


Line l[40],temp;
int N;

bool Can(int k,int obj)
{
	int i;
	for (i=obj+1;i<N; ++i) if (l[k].a[i]=='1') return false;
	return true;
}
int findCan(int k)
{
	int i;
	for (i=k+1;i<N;++i)
	{
		if (Can(i,k)) return i;
	}
}



int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t,st,k;
	int ans,i,j;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d",&N);
		ans = 0;
		for (i=0;i<N;++i)
		{
			scanf("%s",l[i].a);
		}
		for (i=0;i<N;++i)
		{
			if (!Can(i,i))
			{
				k = findCan(i);
				temp = l[k];
				for (j=k;j>i;--j)
				{
					l[j] = l[j-1];
				}
				l[i] = temp;
				ans += (k-i);
			}
		}
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}



