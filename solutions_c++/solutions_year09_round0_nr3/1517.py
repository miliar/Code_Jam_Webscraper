#include<cstdio>
#include<cstring>
#define NMAX 501
#define Mod 10000
using namespace std;
char text[NMAX],pattern[]="welcome to code jam";
int A[NMAX][20],N,M=19,T;

int main()
{
	int t,i,j;

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d ",&T);
	for(t=1;t<=T;++t)
	{
		gets(text);
		N=strlen(text);

		A[N][M]=1;
		for(j=0;j<M;++j)
			A[N][j]=0;

		for(i=N-1;i>=0;--i)
		{
			A[i][M]=1;
			for(j=0;j<M;++j)
			{
				A[i][j]=A[i+1][j];
				if(text[i]==pattern[j])
					A[i][j]=(A[i][j]+A[i+1][j+1])%Mod;
			}
		}

		printf("Case #%d: %04d\n",t,A[0][0]);
	}

	return 0;
}
