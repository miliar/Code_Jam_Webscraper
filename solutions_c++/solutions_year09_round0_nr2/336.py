#include<cstdio>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<queue>

#define FOR(i,a,b) for(int i=(int)(a); i<(int)(b); ++i)
#define FORE(it,C) for(__typeof(C.begin()) it = C.begin(); it!=C.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

using namespace std;

const int nMax = 105;

int N,M;
int tabH[nMax][nMax];
vector<pair<int,int> > tabN[nMax][nMax];
int col[nMax][nMax];

int tabK[4][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};

void makeEdge(int x0, int y0, int x1, int y1) {
	tabN[x0][y0].PB(MP(x1,y1));
	tabN[x1][y1].PB(MP(x0,y0));
}

void dfs(int x, int y, int curCol) {
	if(x<0 || x>=N || y<0 || y>=M)
		return;
	if(col[x][y] != -1)
		return;
		
	col[x][y] = curCol;
	
	FORE(it,tabN[x][y])
		dfs(it->FI, it->SE, curCol);
}

void testcase(int testNr) {
	printf("Case #%d:\n",testNr);
	
	scanf("%d %d",&N,&M);
	FOR(i,0,N) FOR(j,0,M) {
		col[i][j] = -1;
		tabN[i][j].clear();
		scanf("%d",&tabH[i][j]);
	}
	
	FOR(i,0,N) FOR(j,0,M) {
		int bestVal = tabH[i][j];
		int x0=0, y0=0;
		
		FOR(k,0,4) {
			int x1=i+tabK[k][0], y1=j+tabK[k][1];
			if(x1<N && x1>=0 && y1<M && y1>=0 && tabH[x1][y1]<bestVal) {
				bestVal = tabH[x1][y1];
				x0 = x1;
				y0 = y1;
			}
		}
		
		if(bestVal<tabH[i][j])
			makeEdge(i,j,x0,y0);
	}
	
	int curCol = 0;
	FOR(i,0,N) {
		FOR(j,0,M) {
			if(col[i][j] == -1)
				dfs(i, j, curCol++);
			printf("%c ",'a'+col[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int t;
	scanf("%d",&t);
	FOR(i,0,t)
		testcase(i+1);
}
