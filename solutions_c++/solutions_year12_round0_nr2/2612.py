#include <cstdio>
#include <cstring>
const int N=110,MAX=1<<30;
int DP[N][N];
int t[N],p;
inline int max(int a,int b){return a>b?a:b;}
int cans(int a)
{
	if(a<2||a>28)return 0;
	for(int i=0;i<=8;i++)
	{
		int k=a-i-i-2;
		if(k>=i && k<=i+2)
		{
			if(max(i+2,k) >= p)return 2;
			else return 1;
		}
	}
	while(1);
}
inline bool avg(int a)
{return a/3+(a%3!=0) >= p;}
int main()
{
	cans(2);
	int T,w=1,n,s;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&n,&s,&p);
		for(int i=1;i<=n;i++)
			scanf("%d",&t[i]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				DP[i][j]=-MAX;
		printf("Case #%d: ",w++);
		DP[1][0]=avg(t[1]);
		int k=cans(t[1]);
		if(k==1)
			DP[1][1]=0;
		else if(k==2)
			DP[1][1]=1;
		else DP[1][1]=-MAX;
		for(int i=2;i<=n;i++)
		{
			DP[i][0]=DP[i-1][0]+avg(t[i]);
			for(int j=1;j<=i;j++)
			{
				int k=cans(t[i]);
				//printf("%d %d\n",t[i],k);
				if(k==1)
					DP[i][j]=max(DP[i-1][j],DP[i-1][j-1]);
				else if(k==2)
					DP[i][j]=max(DP[i-1][j],DP[i-1][j-1]+1);
				else
					DP[i][j]=DP[i-1][j];
			}
		}
		printf("%d\n",DP[n][s]);
	}
}
