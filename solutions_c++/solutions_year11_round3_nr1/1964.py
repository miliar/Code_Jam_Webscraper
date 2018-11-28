#include <cstdio>
#include <cstring>

#define maxn 55

char s[maxn][maxn];
int n,m;

inline bool paint(int x,int y)
{
	if (x+1==n || y+1==m) return false;
	if (s[x][y+1]!='#') return false;
	if (s[x+1][y]!='#') return false;
	if (s[x+1][y+1]!='#') return false;
	
	s[x][y]='/';s[x][y+1]='\\';
	s[x+1][y]='\\';s[x+1][y+1]='/';
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
			scanf("%s",s[i]);
		bool ok=true;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			if (s[i][j]=='#')
			{
				if (!paint(i,j)) ok=false;
			}
		
		printf("Case #%d:\n",test);
		if (!ok) puts("Impossible");
		else
		{
			for (int i=0;i<n;++i)
				puts(s[i]);
		}
	}
	return 0;
}
