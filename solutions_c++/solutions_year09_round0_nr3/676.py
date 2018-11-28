#include<cstdio>
#include<cstring>
#include<iostream>

#define MOD 10000
#define MAX 500+1

using namespace std;

char S[MAX];
char T[]="welcome to code jam";

int N,M=19;
int DP[MAX][20];

int main()
{
	freopen("C-Large.in","r",stdin);
	freopen("C-Large.out","w",stdout);
	int CSAE;
	scanf("%d",&CSAE);
	getchar();
	for(int Case=1;Case<=CSAE;Case++)
	{
		gets(S);
		N=strlen(S);
		DP[0][0]=1;
		for(int i=1;i<=N;i++)
		{
			DP[i][0]=1;
			for(int j=1;j<=M;j++)
			{
				DP[i][j]=DP[i-1][j];
				if(S[i-1]==T[j-1]) DP[i][j]=(DP[i][j]+DP[i-1][j-1])%MOD;
			}
		}
		printf("Case #%d: %04d\n",Case,DP[N][M]);
	}
	return 0;
}
