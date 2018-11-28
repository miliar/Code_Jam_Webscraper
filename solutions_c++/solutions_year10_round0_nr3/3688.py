#include <iostream>
#include <deque>
using namespace std;

int R, k, N;
int dp[1001][1001];
deque<int> g;
int t, t2, t3;
int c;
int ans;

int main(){
	scanf("%d", &c);
	for (int C = 1; C <= c; C++){
		//memset(dp, 0, sizeof dp);
		g.clear();
		
		scanf("%d %d %d", &R, &k, &N);
		
		for (int i = 0; i < N; i++){
			scanf("%d", &t);
			g.push_back(t);
		}
		
		ans = 0;
		t = 0;
		for (int i = 0; i < R; i++){
			t2 = 0;
			while (t2 < g.size() && t + g.front() <= k){
				t += g.front();
				g.push_back(g.front());
				g.pop_front();
				t2++;
			}
			ans += t;
			t = 0;
		}
		
		printf("Case #%d: %d\n", C, ans);
	}
	return 0;
}
