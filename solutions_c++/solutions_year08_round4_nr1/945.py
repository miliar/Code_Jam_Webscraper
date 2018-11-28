#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
int intrnode,leaf,M,V;
int g[100],c[100],tg[100],tc[100],yu[100];
int dfs(int now)
{
	if(now>intrnode)
		return tg[now];
	if(tg[now]==0)
	return dfs(2*now)||dfs(2*now+1);
	else 
	return dfs(2*now)&&dfs(2*now+1);
}
int main()
{
	int N,ca;
	int i,j;
		freopen("A-small-attempt1.in","r",stdin);
freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		scanf("%d%d",&M,&V);
		intrnode=(M-1)/2,leaf=(M+1)/2;
		int clen=0;
		for(i=1;i<=intrnode;i++)
		{
			scanf("%d%d",&g[i],&c[i]);
			if(c[i])
				yu[++clen]=i;
		}
			for(i=1;i<=leaf;i++)
				scanf("%d",&g[i+intrnode]);

		int	len=(1<<clen);
	//	cout<<len<<endl;
		int mins=1000;
		for(i=0;i<len;i++)
		{
			int e;
			for(e=1;e<=M;e++)
				tg[e]=g[e],tc[e]=c[e];

			int sum=0;
			for(j=0;j<clen;j++)
				if((1<<j)&i)
				{
					tg[yu[j+1]]^=1;
					sum++;
				}
          //   for(j=0;j<clen;j++)
			//	 cout<<tg[j+1]<<endl;
				int v=dfs(1);
				//cout<<v<<endl;
				if(v==V&&sum<mins)
					mins=sum;

		}
			printf("Case #%d: ",ca);
		if(mins==1000)
			printf("IMPOSSIBLE\n");
		else printf("%d\n",mins);
	}
	return 0;
}