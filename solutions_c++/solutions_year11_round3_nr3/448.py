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
		int n,l,h,x;
		vector<int> V;
		scanf("%d%d%d",&n,&l,&h);
		REP(i,n) cin >> x, V.pb(x);
		bool ok = false;
		printf("Case #%d: ",tt+1);
		FOR(now,l,h+1) {
			ok = true;
			REP(i,n) if(V[i] % now != 0 && now % V[i] != 0) ok = false;
			if(ok) {
				printf("%d \n",now);
				goto out;
			}
		}
		printf("NO\n");
		out:;
	}
}


