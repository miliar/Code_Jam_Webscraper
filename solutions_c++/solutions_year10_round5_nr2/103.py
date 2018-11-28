#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef long long ll;

ll l;
int n;
int a[110];
int dp[11000];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%lld%d", &l, &n);
		ll res = 0;
		for(int i=0; i<n; ++i) scanf("%d", &a[i]);
		sort(a, a+n);
		res = (l-10000) / a[n-1];
		l -= (ll)a[n-1]*res;
		dp[0] = 0;
		for(int i=1; i<11000; ++i) dp[i] = 1000000;
		for(int i=0; i<n; ++i)
			for(int j=a[i]; j<11000; ++j)
				dp[j] = min(dp[j], dp[j-a[i]]+1);
		printf("Case #%d: ", iii);
		int wsk = (int)l;
		if(dp[wsk] == 1000000) printf("IMPOSSIBLE\n");
		else printf("%lld\n", res+dp[wsk]);
	}
	return 0;
}
