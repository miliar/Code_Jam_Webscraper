#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 10010

int cases, d[MAXN], l[MAXN], dp[MAXN], n, m;

int main(){
	scanf("%d",&cases);
	for(int xx = 1; xx <= cases; ++xx){
		memset(dp,0,sizeof(dp));
		scanf("%d",&n);
		for(int i = 1; i <= n; ++i){
			scanf("%d%d",&d[i],&l[i]);
		}
		d[0] = 0;
		l[0] = 0;
		++n;
		scanf("%d",&m);
		for(int i = 0; i < n; ++i)
			dp[i] = 99999999;
		dp[1] = 0;
		bool ok = false;
		for(int i = 1; i < n; ++i)
			if(dp[i] != 99999999){
				int t = dp[i];
				int dis = d[i] - d[t];
				if(dis >= l[i]) dis = l[i];
				for(int j = i + 1; j < n; ++j)
					if(d[i] + dis >= d[j])
						dp[j] = min(dp[j], i);
				if(d[i] + dis >= m) ok = true;
			}
		printf("Case #%d: ", xx);
		if(ok) puts("YES");
		else puts("NO");
	}
}
