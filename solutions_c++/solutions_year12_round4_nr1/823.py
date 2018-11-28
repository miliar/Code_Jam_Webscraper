#include <vector>
#include <deque>
#include <iostream>
#include <string>
using namespace std;
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <set>

//By chyx111
#define REP(i,n) for(int n_##__LINE__ = (n), i = 0; i < n_##__LINE__; ++i)

int const N = 10010;
int dp[N];

struct Vine{
	int x, len;
	void scan()
	{
		scanf("%d%d", &x, &len);
	}
};
Vine vine[N];

int main() {
	int ca;
	scanf("%d", &ca);
	REP (ica, ca){
		int n;
		scanf("%d", &n);
		REP (i, n){
			vine[i].scan();
		}
		scanf("%d", &vine[n].x);
		vine[n].len = 0;
		n++;

		memset(dp, -1, (sizeof dp));
		deque<int> deq;
		vector<bool> indeq(n, false);
		deq.push_back(0);
		dp[0] = vine[0].x;
		indeq[0] = true;
		bool updated = false;
		for(; !deq.empty(); ){
			int i = deq.back(); deq.pop_back();
			for(int j = i + 1; j < n; ++j){
				if(vine[i].x + dp[i] < vine[j].x){
					break;
				}else{
					int better = min(vine[j].len, vine[j].x - vine[i].x);
					if(better > dp[j]){
						dp[j] = better;
						if(!indeq[j]){
							deq.push_back(j);
							indeq[j] = true;
						}
					}
				}
			}
			for(int j = i - 1; j >= 0; --j){
				if(vine[i].x - dp[i] > vine[j].x){
					break;
				}else{
					int better = min(vine[j].len, vine[i].x - vine[j].x);
					if(better > dp[j]){
						dp[j] = better;
						if(!indeq[j]){
							deq.push_back(j);
							indeq[j] = true;
						}
					}
				}
			}
			indeq[i] = false;
		}
		printf("Case #%d: ", ica + 1);
		fprintf(stderr, "Case #%d: ", ica + 1);
		puts(dp[n - 1] >= 0 ? "YES" : "NO");
	}
	return 0;
}

