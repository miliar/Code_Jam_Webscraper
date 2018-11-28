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

int const MAXQ=101;

int p;
int q;

int pos[MAXQ];
int wlewo[MAXQ];
int wprawo[MAXQ];

int koszt[MAXQ][MAXQ];

int getKoszt(int a,int b){
	if(b<a||b>=q||a<0) return 0;
	return koszt[a][b];
}

void zrob(int testcase){

	scanf("%d%d",&p,&q);
	REP(i,q) scanf("%d",&pos[i]);

	int lastpos = 0;
	REP(i,q){
		wlewo[i] = pos[i]-lastpos-1;
		lastpos = pos[i];
	}
	lastpos = p+1;
	for(int i=q-1;i>=0;i--){
		wprawo[i] = lastpos-pos[i]-1;
		lastpos=pos[i];
	}

	REP(l,q){
		FOR(a,0,q-l-1){
			int b=a+l;
			koszt[a][b] = INF;
			FOR(i,a,b){
				koszt[a][b]=min(koszt[a][b], 
					getKoszt(a,i-1) + getKoszt(i+1,b) + pos[b] - pos[a] 
					+ wlewo[a] + wprawo[b]);
			}
			//printf("Koszt %d-%d: %d\n",a,b,koszt[a][b]);
		}
	}

	cout << "Case #"<<testcase<<": "<<getKoszt(0,q-1)<<endl;
}

int main() {
	int T; scanf("%d", &T);
	for(int i=1;i<=T;i++) zrob(i);
	return 0;
}


