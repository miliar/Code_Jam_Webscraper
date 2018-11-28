// By mirosuaf v.2.1 modified for CodeJam
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
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
map<pair<int,int>,int> mapa;

int n,m;
char bufor[20][20];

int tab[15*15][15*15*4][15*15*4];
int r[4][2] = { {1,0},{0,1},{-1,0},{0,-1}};
queue<pair<int,pair<int,int> > >q;

void update(int z1, int z2, int z3, int q1, int q2, int q3, int ww){
	if (tab[z1][z2][z3] > tab[q1][q2][q3] + ww) {
		tab[z1][z2][z3] = tab[q1][q2][q3] + ww;
		q.push(make_pair(z1,make_pair(z2,z3)));
	}
}

int shoot(int from, int ruch) {
	if (mapa.find(make_pair(from,ruch))!=mapa.end()) 
		return mapa[make_pair(from,ruch)];
	int px = from/m;
	int py = from%m;
	while ((px >=0) && (px<n)&&(py>=0)&&(py<m)&&(bufor[px][py]!='#')) {
		px += r[ruch][0];
		py += r[ruch][1];
	}
	px -= r[ruch][0];
	py -= r[ruch][1];
	int wyn = (px*m+py)*4+ruch;
	mapa[make_pair(from,ruch)] = wyn;
	return wyn;
}

int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {
	mapa.clear();

scanf("%d%d\n",&n,&m);
REP(i,n) {
	gets(bufor[i]);
}

REP(i,15*15) REP(j,15*15*4) REP(z,15*15*4) tab[i][j][z] = INF;

int startx,starty;
REP(i,n) REP(j,m) if (bufor[i][j]=='O') {startx = i; starty = j; }
int val = shoot(startx*m+starty,0);
tab[startx*m+starty][val][val] = 0;
q.push(make_pair(startx*m+starty,make_pair(val,val)));

while (q.size()!=0) {
	pair<int,pair<int,int > > ww;
	ww = q.front();
	q.pop();
	int tmp[4];
	REP(i,4) tmp[i] = shoot(ww.first,i);
	REP(i, 4) {
		update(ww.first,ww.second.first,tmp[i], ww.first,ww.second.first,ww.second.second,0);
		update(ww.first,tmp[i],ww.second.second, ww.first,ww.second.first,ww.second.second,0);
	}
	REP(ruch,4) {
		int px = (ww.first/m) + r[ruch][0];
		int py = (ww.first%m) + r[ruch][1];
		if ((px >=0) && (px<n)&&(py>=0)&&(py<m)&&(bufor[px][py]!='#')) {
			update(px*m+py,ww.second.first,ww.second.second, ww.first,ww.second.first, ww.second.second,1);
		} else {
			int prt = ww.first*4 + ruch;
			int cel = -1;
			if (ww.second.first == prt) {
				cel = ww.second.second;
			} else if (ww.second.second == prt) cel = ww.second.first;
			if (cel != -1) {
				cel/=4;
				update(cel, ww.second.first, ww.second.second, ww.first,ww.second.first,ww.second.second, 1);
			}
		}
	}
}

int best = INF;
int endval = 0; 
REP(i,n) REP(j,m) if (bufor[i][j] == 'X') { endval = i*m+j; }
REP(i,15*15*4) REP(j,15*15*4) best = min(best, tab[endval][i][j]);
if (best == INF) {
printf("Case #%d: THE CAKE IS A LIE\n",iile);
} else {
printf("Case #%d: %d\n",iile, best);
}
}
return 0;
}

