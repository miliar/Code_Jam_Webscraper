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
#include <cstdlib>
#include <assert.h>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GL ({LL t;scanf(" %lld",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1000000000
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

const int MAXN = 100;

int N,S,p;

int main() {
	int yo=0;
	for (int _=GI;_--;) {
		int cnt=0;
		N=GI,S=GI,p=GI;
		REP (i,N) {
			int test=GI;
			int v,m;
			v=test/3,m=test%3;
			if(m==0) {
				if(v>=p) cnt++;
				else if(S && test>=2 && test<=28) {
					if(v+1>=p) cnt++,S--;
				}
			} else if(m==1) {
				if(v+1>=p) cnt++;
			} else {
				if(v+1>=p) cnt++;
				else if(S && test>=2 && test<=28) {
					if(v+2>=p) cnt++,S--;
				}
			}
		}
		printf("Case #%d: %d\n",++yo,cnt);
	}
	return 0;
}

