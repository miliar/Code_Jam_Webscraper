#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({LL t;scanf(" %lld",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define cl clear()
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

LL N,K;

int main() {
	int yay=0;
	for (int _=GI;_--;) {
		N=GI,K=GI;
		N=1<<N;
		K %= N;
		if(K==N-1) printf("Case #%d: ON\n",++yay);
		else printf("Case #%d: OFF\n",++yay);
	}
	return 0;
}

