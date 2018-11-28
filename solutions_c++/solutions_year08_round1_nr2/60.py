#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FS(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define MK make_pair
#define FI first
#define SE second
typedef long long ll;
typedef long double ldouble;
int n, m;
vector< pair<int,int> > pref[2005];
int ziom[2005], tak[2005];
inline bool koniec() {
	REP(i,m) if(!tak[i]) {
		int zos = 0, tt = 0;
		REP(j,SZ(pref[i])) {
			if(ziom[ pref[i][j].FI ] == pref[i][j].SE) { tt = 1; break; }
		}
		if(!tt) return false;
	}
	return true;
}
inline bool dobrze(int nr) {
	REP(i,m) if(!tak[i]) {
		int zos = 0, tt = 0;
		REP(j,SZ(pref[i])) {
			if(ziom[ pref[i][j].FI ] == pref[i][j].SE) { tt = 1; break; }
			if(ziom[ pref[i][j].FI ] == -1) ++zos;
		}
		if(!tt && !zos) return false;
	}
	return true;
}
bool rek(int gl) {
	if(gl == n) {
		return koniec();
	}
	if(ziom[gl] >= 0) return rek(gl + 1);
	ziom[gl] = 0;
	if(dobrze(gl) && rek(gl + 1)) return true;
	ziom[gl] = 1;
	if(dobrze(gl) && rek(gl + 1)) return true;
	ziom[gl] = -1;
	return false;
}
void lecim(int numer) {
	scanf("%d%d",&n,&m);
	REP(i,n) ziom[i] = -1;
	printf("Case #%d:", numer);
	int blad = 0, zost = m;
	REP(i,m) {
		int t;
		scanf("%d",&t);
		pref[i].clear();
		tak[i] = 0;
		while(t--) {
			int x,y;
			scanf("%d%d",&x,&y);
			pref[i].push_back(make_pair(x-1,y));
		}
	}
	while(!blad) {
		bool zmia = false;
		REP(i,m) if(!tak[i]) {
			int dob = 0, okej = 0;
			vector< pair<int,int> > npr;
			REP(j,SZ(pref[i])) {
				if(ziom[pref[i][j].FI] != -1 && ziom[pref[i][j].FI] == pref[i][j].SE) {
					okej = 1;
					break;
				}
				if(ziom[pref[i][j].FI] == -1) {
					npr.push_back(pref[i][j]);
					++dob;
				}
			}
			if(okej) {
				tak[i] = 1;
				--zost;
				zmia = true;
				continue;
			}
			if(dob == 0) {
				blad = 1;
				break;
			}
			pref[i] = npr;
			if(dob == 1) {
				ziom[pref[i][0].FI] = pref[i][0].SE;
				tak[i] = 1;
				--zost;
				zmia = true;
			}
		}
		if(!zmia) break;
	}
	if(blad || !rek(0)) {
		printf(" IMPOSSIBLE\n");
		return ;
	}
	REP(i,n) printf(" %d", ziom[i]);
	printf("\n");
}
int main() {
	int c;
	scanf("%d",&c);
	REP(i,c) lecim(i+1);
	return 0;
}
