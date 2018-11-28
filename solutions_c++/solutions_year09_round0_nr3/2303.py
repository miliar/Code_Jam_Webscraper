#include<stdio.h>
#include<string.h>

char code[]="welcome to code jam";
char str[505];
int dist[505][25];
int n,m;
int solve()
{
	int i,k;
	n=strlen(code);
	m=strlen(str);
	memset(dist,0,sizeof(dist));
	for(k=0;k<n;k++)
	{
		for(i=0;i<m;i++)
		{
			if(i==0)
				dist[i][k]=0;
			else
				dist[i][k]=dist[i-1][k];
			if(str[i]==code[k])
			{
				if((i!=0)&&(k!=0))
					dist[i][k]+=dist[i-1][k-1];
				else if(k==0)
					dist[i][k]++;
			}
		}
	}
	return dist[m-1][k-1];
}

int main()
{
	int t,T;
	int ans;
//	freopen("sample.in","r",stdin);
 	freopen("test.out","w",stdout);
	scanf("%d",&T);
	gets(str);
	for(t=1;t<=T;t++)
	{
		gets(str);
		ans=solve();
		printf("Case #%d: %.4d\n",t,ans);
	}
	return 0;
}