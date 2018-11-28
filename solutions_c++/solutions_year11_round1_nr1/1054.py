#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>
 
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

int main() {
	int test; scanf("%d",&test); REP(tt,test) {
		LL n;
		int pd,pg;
		scanf("%lld%d%d",&n,&pd,&pg);
		if(n > 100) n = 100;
		//dbg(n); dbg(pd); dbg(pg);i
		bool ok = false;
		for(int i = 1; i <= n; i++) {
			//dbg(i);
			if(pd * i % 100 == 0) {ok = true;}
		}
		if(pd != 100 && pg == 100) ok = false;
		if(pg == 0 && pd != 0) ok = false;
		if(ok) printf("Case #%d: Possible\n",tt+1);
		else printf("Case #%d: Broken\n",tt+1);
	}
}

