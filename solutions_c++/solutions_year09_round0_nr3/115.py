#include <cstdio>
#include <cstring>
#define oo 505
#define Mod 10000
char t[]=" welcome to code jam";
char s[oo];
int f[oo][21];
int N,Test,Case;

inline void Readin()
{
	gets(s+1);
}

inline void Plus(int& A,int B)
{
	A+=B;
	if (A>=Mod) A-=Mod;
}

inline void Solve()
{
	int M=strlen(t+1);
	N=strlen(s+1);
	memset(f,0,sizeof f);
	f[0][0]=1;
	for (int i=0;i<=N;++i)
		for (int j=0;j<=M;++j)
			if (f[i][j])
			{
				if (i<N) Plus(f[i+1][j],f[i][j]);
				if (i<N && j<M && s[i+1]==t[j+1])
					Plus(f[i+1][j+1],f[i][j]);
			}
	
	printf("%.4d\n",f[N][M]);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test),gets(s);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
