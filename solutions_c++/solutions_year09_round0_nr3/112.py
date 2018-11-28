#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
char s[]=" welcome to code jam";
int Test,N,M=19,F[505][20];
char t[520];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&Test);gets(t);
	for (int Case=1;Case<=Test;Case++) {
		gets(t+1);
		memset(F,0,sizeof(F));
		F[0][0]=1;
		N=strlen(t+1);
		for (int i=1;i<=N;i++) {
			F[i][0]=1;
			for (int j=1;j<=M;j++) {
				F[i][j]=F[i-1][j];
				if (t[i]==s[j]) F[i][j]=(F[i][j]+F[i-1][j-1])%10000;
			}
		}
		printf("Case #%d: %.4d\n",Case,F[N][M]);
	}
	return 0;
}
