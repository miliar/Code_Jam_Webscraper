// Maciej Andrejczuk

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <assert.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,p,k) for(int i=(p);i<=(k);i++)
#define FORD(i,p,k) for(int i=(p);i>=(k);i--)
#define ZERO(m) memset(m,0,sizeof(m))
#define PB push_back
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PI;
#define MAXW 100
#define INF 1000000
int n;
int H,W;
int t[MAXW+3][MAXW+3];
int d[MAXW+3][MAXW+3];
int dx[] = { -1,0,0,1 };
int dy[] = { 0,-1,1,0 };

bool outside(int x, int y) {
	if (x<0 || x>=H) return true;
	if (y<0 || y>=W) return true;
	return false;
}

bool bottom(int x, int y) {
	REP(i,4) {
		int px=x+dx[i];
		int py=y+dy[i];
		if (outside(px,py)) continue;
		if (t[x][y]>t[px][py]) return false;
	}
	return true;
}

int solve() {
	
	scanf("%d %d",&H,&W);
	REP(i,H) REP(j,W) {
		scanf("%d",&t[i][j]);
		d[i][j]=0;
	}
	int ile=1;
	queue<PI> q;
	REP(i,H) REP(j,W) {
		if (bottom(i,j)) {
			d[i][j]=ile;
			ile++;
			REP(k,4) {
				q.push(PI(i+dx[k],j+dy[k]));
			}
		}
	}
	REP(pow,200) {
		REP(i,H) REP(j,W) {
			if (d[i][j]>0) continue;
			int mi=INF;
			REP(k,4) {
				if (outside(i+dx[k],j+dy[k])) continue;
				if (t[i+dx[k]][j+dy[k]]<mi)
				{
					d[i][j]=d[i+dx[k]][j+dy[k]];
					mi=t[i+dx[k]][j+dy[k]];
				}
			}
		}
	}
				
	map<int,char> mapa;
	char c='a';
	REP(i,H) {
		REP(j,W) {
			if (mapa[d[i][j]]<'a') {
				mapa[d[i][j]]=c;
				c++;
			}
			printf("%c ",mapa[d[i][j]]);
		}
		printf("\n");
	}
}


int main()
{
	scanf("%d",&n);
	FOR(i,1,n) {
		printf("Case #%d:\n",i);
		solve();
	}
}