#include <cstdio>
#include <cstring>
#define base 10000
#define maxn 505

int f[maxn][50];
char t[]="welcome to code jam",s[maxn];

inline void Plus(int &a,int b)
{
	a+=b;
	if (a>=base) a-=base;
}

int main()
{
	freopen("C_large.in","r",stdin);
	freopen("C_large.out","w",stdout);
	
	int T,test=1;
	int m=strlen(t);
	for (scanf("%d\n",&T);test<=T;++test)
	{
		memset(f,0,sizeof(f));
		f[0][0]=1;
		gets(s);
		int n=strlen(s);
		for (int i=0;i<n;++i)
			for (int j=0;j<=m;++j)
			if (f[i][j])
			{
				Plus(f[i+1][j],f[i][j]);
				if (j<m && s[i]==t[j]) Plus(f[i+1][j+1],f[i][j]);
			}
		
		printf("Case #%d: %04d\n",test,f[n][m]);
	}
	return 0;
}
