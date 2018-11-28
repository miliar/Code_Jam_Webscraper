#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (55)
using namespace std;

int test,N,K;
char s[maxn][maxn],s_[maxn][maxn];
int dx[]={0,-1,-1,-1,0,1,1,1};
int dy[]={-1,-1,0,1,1,1,0,-1};

inline bool Can(int i,int j,int d,int cnt,char c)
{
	if (cnt>=K) return true;
	int xx=i+dx[d],yy=j+dy[d];
	if (xx>=1 && xx<=N && yy>=1 && yy<=N && s[xx][yy]==c) return Can(xx,yy,d,cnt+1,c);
		else return false;
}
int main()
{
	//freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		scanf("%d%d",&N,&K);
		for (int i=1;i<=N;++i) scanf("%s",s[i]+1);
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j) s_[j][N+1-i]=s[i][j];
		
		memcpy(s,s_,sizeof(s_));
		/*for (int i=1;i<=N;++i,puts(""))
			for (int j=1;j<=N;++j) printf("%c",s[i][j]);*/
		for (int i=1;i<=N;++i)
		{
			for (int j=N;j>=1;--j) if (s[j][i]=='B' || s[j][i]=='R')
			{
				char c=s[j][i];
				for (int k=j+1;k<=N;++k) if (s[k][i]=='B' || s[k][i]=='R') break;
					else
					{
						s[k][i]=c;
						s[k-1][i]='.';
					}
			}
		}
		//for (int i=1;i<=N;++i,puts(""))
			//for (int j=1;j<=N;++j) printf("%c",s[i][j]);
		//puts("");
		bool BLUE=false,RED=false;
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j) if (s[i][j]=='B' || s[i][j]=='R')
			{
				bool ok=false;
				for (int k=0;k<8;++k)
					if (Can(i,j,k,1,s[i][j]))
					{
						ok=true;
						break;
					}
				if (ok) 
				{
					if (s[i][j]=='B') BLUE=true;
						else RED=true;
				}
			}
		printf("Case #%d: ",cnt);
		if (RED && BLUE) puts("Both");
		else if (RED) puts("Red");
		else if (BLUE) puts("Blue");
		else puts("Neither");
	}
	return 0;
}
