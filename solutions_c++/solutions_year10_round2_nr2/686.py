#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define REP(i,n) for(int i=0; i < (int)n; i++)
#define REPD(i,n) for(int i=n-1; i >= 0; i--)
#define FOR(i,a,b) for(int i= (int)a; i <= (int)b; i++)
#define FORD(i,a,b) for(int i= (int)a; i >= (int)b; i++)
#define SIZE(x) ((int)(x.size()))
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<long long> vl;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("inputB.txt","r",stdin);
	//freopen("outputB.txt","w",stdout);	

	int numcases;
	scanf("%d",&numcases);
	REP(i,numcases) {
		int n,k,t; ll b; scanf("%d%d%llu%d", &n,&k,&b,&t);
		vl d; REP(j,n) { ll t; scanf("%llu",&t); d.PB(t); }
		vi s; REP(j,n) { int t; scanf("%d",&t); s.PB(t); }
		vl pos; vi spd;
		printf("Case #%d: ", i+1);
		REP(j,n) {
			if(d[j]+t*s[j] >= b) { pos.PB(j); spd.PB(s[j]); }
		}
		if(k==0) { printf("0\n"); continue; }
		if(SIZE(pos) < k || SIZE(pos)==0) {
			printf("IMPOSSIBLE\n"); continue;
		}
		vl pos2;
		FOR(j,SIZE(pos)-k,SIZE(pos)-1) {
			pos2.PB(pos[j]); //cout << pos[j] << endl; 				
		}
		long long res=0;
		REP(j, SIZE(pos2)-1) { 
			res+=(pos2[j+1]-pos2[j]-1)*(j+1);
		}
		res+=(n-1-pos2[(SIZE(pos2)-1)])*SIZE(pos2);
		printf("%llu\n",res);
	}
}
