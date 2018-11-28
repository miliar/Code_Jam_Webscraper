#include<cstdio>
#include<algorithm>
#include<queue>
using namespace std;

#define INF 1000000
#define N 10005
#define node pair<int,int>

node G[N];
int dp[N][2];
int inqueue[N];

inline int left(int i) { return 2*i; } 
inline int right(int i) { return 2*i+1; } 
inline int parent(int i) { return i/2; }
inline int anot(int i) { return i == 0 ? 1 : 0; }

int main(){
	int t;
	scanf("%d",&t);
	for(int testCase = 1; testCase <= t; ++testCase){
		for(int i = 0; i < N; ++i) dp[i][0] = dp[i][1] = INF;
		for(int i = 0; i < N; ++i) inqueue[i] = 0;
		int m,v;
		scanf("%d %d",&m, &v);
		
		queue<int> Q;
		vector<int> h;
		for(int i = 1; i <= (m-1)/2; ++i){
			scanf("%d %d",&G[i].first, &G[i].second);
		}
		for(int i = (m+1)/2; i <= m; ++i){
			scanf("%d",&G[i].first);
			dp[i][G[i].first] = 0;
			int anot = G[i].first == 0 ? 1 : 0;
			dp[i][anot] = INF;
			inqueue[i] = 1;
			if (!inqueue[parent(i)]) h.push_back(parent(i));
		}
		sort(h.begin(), h.end());
		for(int i = h.size()-1; i >=0; i--) if(!inqueue[h[i]]){
			Q.push(h[i]);
			inqueue[h[i]] = 1;
		}
		

		while(!Q.empty()){
			int p = Q.front();
			Q.pop();
			int l = left(p);
			int r = right(p);
			//printf("p = %d\n", p);
			if (G[p].second == 0){//not change
				//printf("%d not change (%d, %d)!\n", p, l, r);
				if (G[p].first == 1){//AND
					dp[p][1] = min(INF, dp[l][1] + dp[r][1]);
					dp[p][0] = min(INF, min(dp[l][0]+dp[r][0], min(dp[l][1]+dp[r][0], dp[r][1]+dp[l][0])));
				}
				if (G[p].first == 0){//OR
					//printf("or gate!\n");
					dp[p][1] = min(INF, min(dp[l][1]+dp[r][1], min(dp[l][1]+dp[r][0], dp[r][1]+dp[l][0])));
					dp[p][0] = min(INF, dp[l][0] + dp[r][0]);
				}
			}
			else{//change
				int a[2][2];
				a[0][0] = min(INF, dp[l][0] + dp[r][0]);
				a[0][1] = min(INF, min(dp[l][1] + dp[r][1], min(dp[l][1] + dp[r][0], dp[r][1] + dp[l][0])));
				a[1][0] = min(INF, min(dp[l][0] + dp[r][0], min(dp[l][1] + dp[r][0], dp[r][1] + dp[l][0])));;
				a[1][1] = min(INF, dp[l][1] + dp[r][1]);

				if (G[p].first == 1){//and
					dp[p][1] = min(a[1][1], a[0][1]+1);
					dp[p][0] = min(a[1][0], a[0][0]+1);
				}
				else{
					dp[p][1] = min(a[0][1], a[1][1] + 1);
					dp[p][0] = min(a[0][0], a[1][0] + 1);
				}
			}
			//queue
			if(!inqueue[parent(p)] && p!=1){
				inqueue[parent(p)] = 1;
				Q.push(parent(p));
			}
		}
		//for(int i = m; i >= 1; --i) printf("%d =>\t%d %d\n", i, dp[i][0], dp[i][1]);

		printf("Case #%d: ", testCase);
		if (dp[1][v] < INF) printf("%d\n",dp[1][v]); 
		else printf("IMPOSSIBLE\n");
	}


}
