#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int dx[]={0,1,1,1};
const int dy[]={1,0,1,-1};
int Test,Case,N,M;
char St[100],Map[100][100];
bool FB,FR;

inline bool Check(char C)
{
	for (int i=0;i<N;i++)
	for (int j=0;j<N;j++)
	if (Map[i][j]==C) {
		for (int k=0;k<4;k++) {
			int x=i,y=j,z=0;
			for (;x>=0 && y>=0 && Map[x][y]==C;z++,x+=dx[k],y+=dy[k]);
			if (z>=M) return true;
		}
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d",&N,&M);
		memset(Map,0,sizeof(Map));
		for (int i=0;i<N;i++) {
			scanf("%s",St);
			for (int j=N-1,k=N-1;j>=0;j--) {
				for (;j>=0 && St[j]=='.';j--);
				if (j<0) break;
				Map[i][k--]=St[j];
			}
		}
		FR=Check('R');
		FB=Check('B');
		printf("Case #%d: ",++Case);
		if (FR && FB) printf("Both\n");
		else if (FR) printf("Red\n");
		else if (FB) printf("Blue\n");
			else printf("Neither\n");
	}
	return 0;
}
