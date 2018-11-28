#include <stdio.h>
#include <algorithm>
using namespace std;

int d[110][2];
int f[2][110];

int maxd(int a,int b,int c)
{
	return max(max(abs(a-b),abs(b-c)),abs(c-a));
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,C=0;
	scanf("%d",&T);
	while(++C<=T)
	{
		printf("Case #%d: ",C);
		memset(d,-1,sizeof(d));
		int N,S,p;
		scanf("%d %d %d",&N,&S,&p);
		int i,j;
		int pre=0,now=1;
		memset(f[pre],-1,sizeof(f[pre]));
		f[pre][0]=0;
		for(i=0;i<N;i++)
		{
			memset(f[now],-1,sizeof(f[now]));
			int t,a,b,c;
			scanf("%d",&t);
			for(a=max(0,t/3-2);a<=t/3;a++)
			{
				for(b=a;b<=min(10,(t-a)/2) && b<=a+2;b++)
				{
					c=t-a-b;
					if(c<0 || c>10)continue;
					int g=maxd(a,b,c);
					int m=max(max(a,b),c);
					if(g==2)d[i][1]=max(d[i][1],(int)(m>=p));
					if(g<2)d[i][0]=max(d[i][0],(int)(m>=p));
				}
			}
			for(j=0;j<=S;j++)
			{
				f[now][j]=f[pre][j];
				if(~d[i][0] && ~f[pre][j])f[now][j]=max(f[now][j],f[pre][j]+d[i][0]);
				if(j>0 && ~d[i][1] && ~f[pre][j-1])f[now][j]=max(f[now][j],f[pre][j-1]+d[i][1]);
			}
			swap(pre,now);
		}
		printf("%d\n",f[pre][S]);
	}
	return 0;
}
