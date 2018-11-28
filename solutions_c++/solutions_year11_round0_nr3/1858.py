#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

const int INF = 1000000000;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

const int LIMIT = 1<<20;

int dp[LIMIT];
int nums[1024];
int N;

int main() {
	OPEN("C");
	REP(i,LIMIT) dp[i] = INF + 1;
	int T = getint();
	REP(loop,T) {

		N=getint();
		REP(i,N) nums[i]=getint();
		sort(nums,nums+N);

		int xorSum = 0;
		int ans = 0;
		REP(i,N) xorSum ^= nums[i];
		if(xorSum!=0) ans=-1;
		else {
			int minV = INF;
			int maxV = -INF;
			int totalSum = 0;
			REP(i,N) {
				int x = nums[i];
				totalSum += x;
				FORD(j,maxV,minV) {
					if(dp[j]>INF) continue;
					int k = j ^ x;
					if(k >= LIMIT) continue;
					if(dp[j]+x<dp[k]) {
						dp[k] = dp[j]+x;
						if(k<minV)minV=k;
						if(k>maxV)maxV=k;
					}
				}
				if(x<dp[x]) {
					dp[x] = x;
					if(x<minV)minV=x;
					if(x>maxV)maxV=x;
				}
			}

			int best = INF + 1;
			FOR(i,minV,maxV) {
				best=min(best,dp[i]);
				dp[i]=INF+1;
			}
			ans = totalSum - best;
		}

		char s[16];
		if(ans==-1) sprintf(s,"NO");
		else sprintf(s,"%d",ans);
		printf("Case #%d: %s\n",loop+1,s);
	}
	return 0;
}
