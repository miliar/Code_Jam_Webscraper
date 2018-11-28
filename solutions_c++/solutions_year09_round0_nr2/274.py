#define MD(x) if (0) {x;}
#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
using namespace std;

const int maxN = 110;
typedef pair<int,int> PI;
typedef pair<int,PI> node;

int G[maxN][maxN];
char M[maxN][maxN];
bool sink[maxN][maxN];
node d[maxN*maxN];
PI flow[maxN*maxN];

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

int main(){
	int tc,R,C;
	scanf("%d",&tc);
	for (int ti=1; ti<=tc; ti++){
		scanf("%d%d",&R,&C);
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++){
				scanf("%d",&G[i][j]);
				d[i*C+j] = node(G[i][j],PI(i,j));
			}

		memset(sink,false,sizeof(sink));
		int N = R*C;
		sort(d,d+N);
		MD(printf("d:");for (int i=0; i<N; i++)printf("(%d,%d,%d) ",d[i].first,d[i].second.first,d[i].second.second);
				printf("\n");)

		for (int i=0; i<N; i++){
			int x = d[i].second.first, y = d[i].second.second;
			flow[i] = d[i].second;
			for (int r=0; r<4; r++){
				int x2 = x+dx[r], y2 = y+dy[r];
				if (x2<0 || x2==R || y2<0 || y2==C) continue;
				if (d[i].first>G[x2][y2]){
					d[i].first = G[x2][y2];
					flow[i] = PI(x2,y2);
				}
			}
			if (flow[i]==d[i].second) sink[x][y]=true;
		}
		MD(printf("flow:");for (int i=0; i<N; i++)printf("(%d,%d,%d) ",i,flow[i].first,flow[i].second);
				printf("\n");)

		char ch='a';
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++)
				if (sink[i][j]) M[i][j] = ch++;
		for (int i=0; i<N; i++){
			int x = d[i].second.first, y = d[i].second.second;
			int x2 = flow[i].first, y2 = flow[i].second;
			M[x][y] = M[x2][y2];
		}
		map<char,char>mp;
		ch = 'a';
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++){
				if (mp.count(M[i][j])==false) mp[M[i][j]] = ch++;
				M[i][j] = mp[M[i][j]];
			}
		printf("Case #%d:\n",ti);
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++)
				if (j+1==C) printf("%c\n",M[i][j]);
				else printf("%c ",M[i][j]);
	}
	


	return 0;
}
