#include "stdio.h"
int boo[10],n,m,conn[10][10],ok,x[10],p[10],q[10];
void search(int now)
{
	int k,i;
	if(now==m+1)
	{
		for(i=0;i<m-1;i++)
			if(conn[x[p[i]]][x[q[i]]]==0)
				return;
		ok=1;
		return;
	}
	for(i=1;i<=n;i++)
		if(boo[i]==0)
		{
			boo[i]=1;	
			x[now]=i;
			search(now+1);
			if(ok==1)
				return;
			boo[i]=0;
		}
}
int main()
{
	int tot,kase,i,k,j;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			for(k=1;k<=n;k++)
				conn[i][k]=0;
		for(i=0;i<n-1;i++)
		{
			scanf("%d%d",&k,&j);
			conn[k][j]=1;
			conn[j][k]=1;
		}
		scanf("%d",&m);
		for(i=0;i<m-1;i++)
			scanf("%d%d",&p[i],&q[i]);
		ok=0;
		for(i=1;i<=n;i++)
			boo[i]=0;
		search(1);
		printf("Case #%d: ",kase);
		if(ok==0)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
