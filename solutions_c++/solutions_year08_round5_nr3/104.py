#include <cstdio>
#include <memory>
#define odd(x) ((x)&1)
#define oo 85
bool map[oo][oo];
bool mk[oo][oo];
int x[oo][oo],y[oo][oo];
int Test,Case;
int N,M;
char s[oo];
const int dx[]={-1,-1,0,0,1,1};
const int dy[]={-1,1,-1,1,-1,1};
#define ok(x,y) ((x)>0&&(x)<=N&&(y)>0&&(y)<=M&&!map[x][y])

inline bool Extend_Path(int i,int j)
{
	for (int k=0,I,J;k<6;++k)
	{
		I=dx[k]+i,J=dy[k]+j;
		if (ok(I,J) && !mk[I][J])
		{
			mk[I][J]=true;
			if (!x[I][J] || Extend_Path(x[I][J],y[I][J]))
			{
				x[I][J]=i;
				y[I][J]=j;
				return true;
			}
		}
	}
	return false;
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&Test);Test;Test--)
	{
		scanf("%d%d",&N,&M);
		
		int ans=0;
		for (int i=1;i<=N;++i)
		{
			scanf("%s",s+1);
			for (int j=1;j<=M;++j)
			{
				map[i][j]=s[j]=='x';
				ans+=!map[i][j];
			}
		}
		
		memset(x,0,sizeof x);
		memset(y,0,sizeof y);
		for (int i=1;i<=N;++i)
			for (int j=1;j<=M;++j)
				if (!map[i][j] && odd(j))
				{
					memset(mk,0,sizeof mk);
					if (Extend_Path(i,j)) ans--;
				}
		
		printf("Case #%d: %d\n",++Case,ans);
	}
	
	return 0;
}
