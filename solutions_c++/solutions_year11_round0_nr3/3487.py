#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<cstring>
#include<iostream>
#include<sstream>
using namespace std;
 
#define PB push_back
#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)
#define SZ(x) int((x).size())
#define REP(i,n) for(int i=0,_=(n);i<_;++i)
#define FOR(i,a,b) for(int i=(a),_=(b);i<=_;++i)
#define FORD(i,a,b) for(int i=(a),_=(b);i>=_;--i)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int INF=1e9+9;

int t[1001];

void inline jeden() {
	int n, sum = 0, x = 0;
	scanf("%d", &n);
	REP (i, n) {
	  scanf("%d", t + i);
	  sum += t[i];
	  x ^= t[i];
	}
	int mn = *min_element(t, t + n);
	if (x == 0) {
	  printf("%d\n", sum - mn);
	} else {
	  puts("NO");
	}
}

int main() {
	int z;scanf("%d",&z);FOR(i, 1, z) {
	  printf("Case #%d: ", i);
	jeden();
	}
}
