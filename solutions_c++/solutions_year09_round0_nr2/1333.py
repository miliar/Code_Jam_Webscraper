//By mirosuaf v.2.1 modified for CodeJam
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
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
const int MAXN = 127;
typedef vector<int> VI; 

const int tab[4][2]={
		{-1,0},
		{0,-1},
		{0, 1},
		{1, 0} };


int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
		int t[MAXN][MAXN],numer[MAXN][MAXN];
		vector<pair<int,int> > rnum;
		VI sas[MAXN*MAXN];
		REP(i,MAXN) {
			REP(j,MAXN) {
				numer[i][j]=-1;
				t[i][j]=INF;
			}
			sas[i].clear();
		}
		int n,m,nmb=0;
		scanf("%d%d",&n,&m);
		FOR(i,1,n) FOR(j,1,m) {
			numer[i][j]=nmb;
			rnum.push_back(make_pair(i,j));
			nmb++;
			scanf("%d",&t[i][j]);
		}
		
		FOR(i,1,n) {
			FOR(j,1,m) {
				int polacz = -1;
				vector<pair<int,int> >  v;
				REP(k,4) v.push_back(make_pair(t[i+tab[k][0]][j+tab[k][1]],numer[i+tab[k][0]][j+tab[k][1]])); 
				REP(k,4) if (v[k].first>=t[i][j]) v[k]=make_pair(INF,-1); 
				sort(v.begin(),v.end());
				if (v[0].first!=v[1].first) polacz = v[0].second; else
					REP(k,4) if (t[i+tab[k][0]][j+tab[k][1]]==v[0].first && polacz == -1) polacz = numer[i+tab[k][0]][j+tab[k][1]];
				if (polacz!=-1) {
					sas[polacz].push_back(numer[i][j]);
					sas[numer[i][j]].push_back(polacz);
				}
			}
		}
		char used[MAXN][MAXN]; REP(i,MAXN) REP(j,MAXN) used[i][j]='?';
		char alfabet = 'a';
		FOR(i,1,n) {
			FOR(j,1,m) if (used[i][j]=='?') {
				used[i][j]=alfabet;
				alfabet++;
				queue<pair<int,int> > kolej;
				kolej.push(make_pair(i,j));
				while (!kolej.empty()) {
					int _i = kolej.front().first;
					int _j = kolej.front().second;
					kolej.pop();
					REP(ii,sas[numer[_i][_j]].size()) {
						int sel = sas[numer[_i][_j]][ii];
						int px = rnum[sel].first;
						int py = rnum[sel].second;
						
						if (used[px][py]=='?') {
							used[px][py]=used[i][j];
							kolej.push(make_pair(px,py));
						}
					}
				}
			}
		}
		printf("Case #%d: \n",iile);
		FOR(i,1,n) {
			FOR(j,1,m) {
				printf("%c",used[i][j]);
				if (j==m) printf("\n"); else printf(" ");
			}
		}

	}
	return 0;
}

