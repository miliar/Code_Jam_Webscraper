#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn=1000+10;
int opt[11][maxn][maxn];
int w[maxn][maxn];
int test;

int main()
{
	//freopen("input.txt","r",stdin);

	for (int c=2;c<=10;c++)
	{
		for (int len=3;len<=1000;len++)
		for (int i=1,j=len;j<=1000;i++,j++)
		{
			if (i*c>=j) opt[c][i][j]=0;
			else
			{
				opt[c][i][j]=1000000000;
				for (int k=i+1;k<j;k++)
					opt[c][i][j]<?=max(opt[c][i][k],opt[c][k][j])+1;
			}
		}
		//printf("%d\n",c);
	}
			
	scanf("%d",&test);
	for (int t=0;t<test;t++)
	{
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		printf("Case #%d: %d\n",t+1,opt[c][a][b]);
	}
}
