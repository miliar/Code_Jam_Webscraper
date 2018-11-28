#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int N,mod=10000,F[510][25];
char str[700],s[25];

bool num(char s)
{
	return s>='0' && s<='9';
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	strcpy(s,"welcome to code jam");
	int T=0,i,j,M=strlen(s),t;
	gets(str);
	i=0;
	while(num(str[i])) 
	{
		T=T*10+str[i]-'0';
		i++;
	}
	for(t=1;t<=T;t++)
	{
		gets(str);
		N=strlen(str);
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
			{
				if(i>0) F[i][j]=F[i-1][j];
				else F[i][j]=0;
				if(str[i]==s[j])
				{
					if(j>0)
					{
						if(i>0) F[i][j]=(F[i][j]+F[i-1][j-1])%mod;
					}
					else F[i][j]=(F[i][j]+1)%mod;
				}
			}
		printf("Case #%d: ",t);
		if(F[N-1][M-1]<10) printf("000");
		else if(F[N-1][M-1]<100) printf("00");
		else if(F[N-1][M-1]<1000) printf("0");
		printf("%d\n",F[N-1][M-1]);
	}
	return 0;
}