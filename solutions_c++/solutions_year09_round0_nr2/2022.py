// Marek Rogala; Code Jam 2009
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=101;

int h,w;
int wys[MAXN][MAXN],zlew[MAXN][MAXN];
int zlewid;

bool valid(int x, int y){
return 0<=x&&x<h&&0<=y&&y<w;
}

int znajdz(int x, int y){
	if(zlew[x][y]!=-1) return zlew[x][y];
	int minsas=1000000, mx,my;
	if(valid(x-1,y)&&wys[x-1][y]<minsas) {
		mx=x-1;
		my=y;
		minsas=wys[x-1][y];
	}
	 if(valid(x,y-1)&&wys[x][y-1]<minsas) {
		mx=x;
		my=y-1;
		minsas=wys[x][y-1];
	}
	 if(valid(x,y+1)&&wys[x][y+1]<minsas) {
		mx=x;
		my=y+1;
		minsas=wys[x][y+1];
	}
	 if(valid(x+1,y)&&wys[x+1][y]<minsas) {
		mx=x+1;
		my=y;
		minsas=wys[x+1][y];
	} 

	if(minsas<wys[x][y]){
		zlew[x][y] = znajdz(mx,my);
	}else {
		zlew[x][y] = zlewid++;
	}
 	return zlew[x][y];
}

void zrob(int t){
	scanf("%d%d",&h,&w);
	REP(i,h)
		REP(j,w){
				scanf("%d", &wys[i][j]);
				zlew[i][j]=-1;
			}
	zlewid=0;
	printf("Case #%d:\n",t);
	REP(i,h){
		REP(j,w)
			printf("%c ",'a'+znajdz(i,j));
		printf("\n");
	}
	
}

int main() {
	int T; scanf("%d", &T); 
	FOR(i,1,T) zrob(i);
	return 0;
}


