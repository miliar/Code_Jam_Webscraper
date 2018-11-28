#include<cstdio>
#include <algorithm>
using namespace std;

/*
‚Ç‚ê‚­‚ç‚¢‰“‚­‚Ü‚Å‚¢‚¯‚éH
êŠ‚É‚æ‚é‚¯‚Ç
‚Ä‚«‚Æ[‚É‚â‚ê‚Î‹‚ß‚ç‚ê‚éB
*/

int T;
int N, D;
int d[10000], l[10000];
pair<int, int> st[10000];
int dp[10000];

int main()
{
	scanf("%d", &T);
	for(int t=0;t<T;){
		printf("Case #%d: ", ++t);

		scanf("%d", &N);
		for(int j=0;j<N;j++){
			scanf("%d%d", d+j, l+j);
			st[j] = make_pair(d[j], l[j]);
		}
		for(int j=0;j<N;j++) dp[j] = -1;
		scanf("%d", &D);
		sort(st, st+N);

		bool flg = false;
		dp[0] = d[0];
		for(int i=0;i<N;i++){
			for(int j=i+1;j<N;j++){
				if(st[j].first > st[i].first && st[j].first <= st[i].first+dp[i]){
					dp[j] = max(dp[j], min(st[j].first - st[i].first, st[j].second));
				}
			}
			//printf("%d:%d\n", i, dp[i]);
			if(st[i].first + dp[i] >= D) flg = true;
		}

		puts(flg ? "YES" : "NO");
	}

	return 0;
}
