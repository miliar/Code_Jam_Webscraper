#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
using namespace std;
int n;
struct vine{
	int len;
	int st;
}v[10001];
int cmp(vine a,vine b)
{
	return a.st<b.st;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,cas=1,i,len,j;
	scanf("%d",&t);
	while(t--)
	{
		bool flag=0;
		int le[10001];
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d %d",&v[i].st,&v[i].len);
		sort(v,v+n,cmp);
		scanf("%d",&len);
		printf("Case #%d: ",cas++);
		int l=v[0].st,m=0;
		memset(le,0,sizeof(le));
		le[0]=v[0].st;
		for(i=0;i<n;i++)
		{
			if(v[i].st+le[i]>=len)
			{
				flag=1;
				break;
			}
			for(j=i+1;j<n && v[j].st-v[i].st<=le[i] ;j++)
				if(le[j]==0)
					le[j]=min(v[j].st-v[i].st,v[j].len);
		}
		if(!flag)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
