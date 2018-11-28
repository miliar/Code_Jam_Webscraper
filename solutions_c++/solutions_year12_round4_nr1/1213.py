#include<iostream>
#include<stdio.h>

#include<string.h>

using namespace std;

int maxx(int a,int b)
{
    return a>b?a:b;
}
int n;
int l[10005],d[10005];
int dis[10005];
int len;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int p,i,j,k,t;
	int flag,casenum=1;
        
	scanf("%d",&t);
        for(casenum=1;casenum<=t;casenum++)
	{
		flag=0;
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&len);
		memset(dis,0,sizeof(dis));
		dis[0]=d[0];
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++)
			{
				if (dis[i]+d[i]>=d[j])
				{
					if (l[j]>=d[j]-d[i])
						dis[j]=maxx(dis[j],d[j]-d[i]);
					else
						dis[j]=maxx(dis[j],l[j]);
				}else continue;
			}
		}
		for (i=0;i<n;i++)
			if (d[i]+dis[i]>=len)
				flag=1;
        printf("Case #%d: ",casenum);
		if (flag==1)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
