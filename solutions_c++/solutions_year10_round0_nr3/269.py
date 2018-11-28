#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
typedef long long LL;

int main(){
	int T;
	cin >> T;
	FORE(z,1,T){
		LL R,k,N;
		cin >> R >> k >> N;
		LL g[N];
		FOR(i,0,N)
			cin >> g[i];
		LL to[N], done[N];
		FOR(i,0,N){
			LL ttl = g[i], cur=i;
			while (1){
				cur = (cur+1)%N;
				if (cur==i) break;
				if (ttl+g[cur]>k) break;
				ttl += g[cur];
			}
			to[i] = cur;
			done[i] = ttl;
		}
		LL ans = 0, cur = 0;
		FOR(x,0,R){
			ans += done[cur];
			cur = to[cur];
		}
		printf("Case #%d: %lld\n",z,ans);
	}
	return 0;
}
