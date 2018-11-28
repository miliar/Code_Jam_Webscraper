#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(0)printf

#define MAXV 100000

int t[20000];
int c[20000];
int M, V;

int min_changes(int node, int val) {
	if (node>(M-1)/2) {
		if (val!=t[node]) return MAXV;
		else return 0;
	}

	int l0=min_changes(node*2, 0);
	int l1=min_changes(node*2, 1);
	int r0=min_changes(node*2+1, 0);
	int r1=min_changes(node*2+1, 1);

	int minn[2][2];

	minn[1][0]=min(l0+r0, l0+r1);
	minn[1][0]=min(minn[1][0], l1+r0);
	minn[1][1]=l1+r1;
	
	minn[0][1]=min(l0+r1, l1+r0);
	minn[0][1]=min(minn[0][1], l1+r1);
	minn[0][0]=l0+r0;

	int res=minn[t[node]][val];
	if (c[node]) {
		res=min(res, minn[1-t[node]][val]+1);
	}
	return res;
}


int main() {
	int ncaso;
	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		scanf(" %d %d", &M, &V);
		FOR(i, 1, (M-1)/2) {
			scanf(" %d %d", &t[i], &c[i]);
			if (t[i]!=1) t[i]=0;
			if (c[i]!=1) c[i]=0;
		}
		REP(i, (M+1)/2) {
			scanf(" %d", &t[i+1+(M-1)/2]);
		}
		int res=min_changes(1, V);
		if (res>=MAXV) cout << "IMPOSSIBLE" << endl;
		else	cout << res << endl;
	}

	return 0;
}
