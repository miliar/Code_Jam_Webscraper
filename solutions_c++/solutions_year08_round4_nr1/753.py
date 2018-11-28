#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <string>

using namespace std;

#define go(i,v) for(typeof(v.begin()) i=v.begin();i!=v.end();i++)
#define fo(i,n) for(int i=0;i<n;i++)
#define fi fo(i,n)
#define fj fo(j,n)
#define all(v) v.begin(),v.end()

inline int get(void) { int x; scanf("%d",&x); return x; }

#define MAX_N 10000
#define INF (1<<25)

#define AND_GATE 1
#define OR_GATE 0
#define CHANGEABLE 1

int cached[MAX_N][2];
int dp[MAX_N][2],g[MAX_N],c[MAX_N],val[MAX_N];
#define LEFT(x) ((x)*2+1)
#define RIGHT(x) ((x)*2+2)
int memo(int i,int v) {
	if(cached[i][v]) return dp[i][v];
	cached[i][v]=1;
	int& cache = dp[i][v];

	cache = INF;
#define aoeu(x) cache = min(cache, x)

	if(val[i]==-1) { // gate.
		
		for(int t=0;t<2;t++)
			if(g[i]==t||c[i]){
				int add = (g[i]!=t?1:0);

				if(t==AND_GATE) {
					if(v) aoeu(memo(LEFT(i),1) + memo(RIGHT(i),1) + add);
					else {
						aoeu(memo(LEFT(i),0) + memo(RIGHT(i),0) + add);
						aoeu(memo(LEFT(i),0) + memo(RIGHT(i),1) + add);
						aoeu(memo(LEFT(i),1) + memo(RIGHT(i),0) + add);
					}
				} else {
					if(v) {
						aoeu(memo(LEFT(i),1) + memo(RIGHT(i),1) + add);
						aoeu(memo(LEFT(i),0) + memo(RIGHT(i),1) + add);
						aoeu(memo(LEFT(i),1) + memo(RIGHT(i),0) + add);
					}
					else {
						aoeu(memo(LEFT(i),0) + memo(RIGHT(i),0) + add);
					}
				}
			}

	} else { // end.
		if(v == val[i]) cache = 0;
	}

	return cache;
}
int soln(){
	int n = get();
	int want=get();
	memset(cached,0,sizeof(cached));
	fo(i,(n-1)/2) { g[i] = get(); c[i] = get();}
	fi val[i] = -1;
	fo(i,(n+1)/2) { val[(n-1)/2+i] = get(); }
	return memo(0,want);
}

int main(void){
	int n = get();
	for(int i=1;i<=n;i++){
		int ans=soln();
		if(ans==INF) printf("Case #%d: %s\n",i,"IMPOSSIBLE");
		else         printf("Case #%d: %d\n",i,ans);
	}
}
