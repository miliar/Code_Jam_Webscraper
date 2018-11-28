#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
struct S
{
	int lh;
	int rh;
}s[1005];
int n;
int cmp(const S a,const S b)
{
	return a.lh<b.lh;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("f.out","w",stdout);
	int i,j,k;
	int T;
	int case_cnt=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&s[i].lh,&s[i].rh);
		std::sort(s,s+n,cmp);
		int res=0;
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if( (s[i].lh-s[j].lh)*(s[i].rh-s[j].rh)<0)
					res++;
			}
		}
		printf("Case #%d: %d\n",++case_cnt,res);
	}
}