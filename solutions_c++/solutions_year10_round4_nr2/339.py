#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

const int MAXN = 1<<10;
LL koszt[MAXN*2][12];
int wymagania[MAXN*2];
int kasa[MAXN*2];

void testcase(int v) {
	printf("Case #%d: ", v);
	int p;
	scanf("%d", &p);
	int rozmiar = (1<<p);
	REP(i,rozmiar) scanf("%d", wymagania+i);
	reverse(wymagania,wymagania+rozmiar);
	FORD(i,rozmiar-1,1) scanf("%d", kasa+i);
	REP(i,rozmiar*2) FOR(j,0,p)
		koszt[i][j] = INT_MAX;
	FOR(i,rozmiar,rozmiar*2-1) {
		FOR(j,0,p) koszt[i][j] = INT_MAX;
		wymagania[i-rozmiar] = p-wymagania[i-rozmiar];
		FOR(j,wymagania[i-rozmiar],p) koszt[i][j] = 0;
	}
	FORD(i,rozmiar-1,1) {
		FOR(j,0,p) {
			if(j != 0) koszt[i][j] = min(koszt[i][j], koszt[i][j-1]);
			koszt[i][j] = min(koszt[i][j], koszt[2*i][j] + koszt[2*i+1][j]);
			if(j != p) {
				koszt[i][j] = min(koszt[i][j], koszt[2*i][j+1] + koszt[2*i+1][j+1] + (LL)kasa[i]);
			}
		}
	}
	printf("%lld\n", koszt[1][0]);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

