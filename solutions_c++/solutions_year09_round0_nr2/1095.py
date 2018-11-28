#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;

int T,H,W;
#define MAXN 107
int pl[MAXN][MAXN];
int out[MAXN][MAXN];

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

int go(int x,int y){
	if(out[x][y] == 0){
		int mi=999999;
		REP(k,4) mi=min(mi,pl[x+dx[k]][y+dy[k]]);
		REP(k,4) if(mi == pl[x+dx[k]][y+dy[k]]){
			out[x][y]= go(x+dx[k],y+dy[k]);
			break;
		}
	}
	return out[x][y];
}

int main(){
	cin >> T;
	FOR(cas,1,T){
	REP(i,MAXN) REP(j,MAXN) pl[i][j]=999999;
		cin >> H >> W;
		FOR(i,1,H) FOR(j,1,W) cin >> pl[i][j];
		//
		int ak=1;
		FOR(x,1,H) FOR(y,1,W){
			bool sink=true;
			REP(k,4) if(pl[x+dx[k]][y+dy[k]] < pl[x][y]) sink=false;
			out[x][y]=(sink ? ak++ : 0);
		}
//		FOR(x,1,H) {FOR(y,1,W) cout << out[x][y] << " "; cout << endl;}
		FOR(x,1,H) FOR(y,1,W) go(x,y);
		//
		cout << "Case #" << cas << ": " << endl;
		map<int, char> M;
		char aka='a';
		FOR(i,1,H){
			FOR(j,1,W){
				if(!M.count(out[i][j])) M[out[i][j]]=aka++;
				cout << M[out[i][j]] << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
