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
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;
#define N (1<<20)

int dp[2][N];
int *cur=dp[0], *old=dp[1];

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int n;
		cin >> n;
		memset(old,-1,N*4);
		old[0]=0;
		int xr=0;
		int sum=0;
		FOR(i,0,n){
			copy(old,old+N,cur);

			int x;
			cin >> x;
			xr ^= x;
			sum += x;
			FOR(r,0,N)
				if (old[r]>=0) 
				if (!(i==n-1&&old[r]+x==sum))
					cur[r^x]=max(cur[r^x],old[r]+x);
			swap(old,cur);
		}
		int ans = -1;
		FOR(i,0,N)
			if (old[i]>0 && old[xr^i]>0 && xr==0) ans=max(ans,old[i]);
//		printf("xor %d\n",xr);
//		FOR(i,0,16) printf("%d ",old[i]); puts("");
		printf("Case #%d: ",z);
		if (ans==-1) puts("NO");
			else printf("%d\n",ans);
	}
	return 0;
}
