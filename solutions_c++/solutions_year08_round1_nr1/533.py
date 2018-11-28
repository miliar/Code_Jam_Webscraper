#include <stdio.h>
#include <algorithm>
#define MAXN 1000

using namespace std;
int main()
{
	int icase, ncase;
	long long int first[MAXN], second[MAXN];
	int i, n;
	long long int ans;
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d", &n);
		for(i=0; i<n; ++i)
			scanf("%lld", &first[i]);
		for(i=0; i<n; ++i)
			scanf("%lld", &second[i]);
		sort(first, first+n);
		sort(second, second+n);
		ans = 0;
		for(i=0; i<n; ++i)
			ans += first[i] * second[n-1-i];
		printf("Case #%d: %lld\n", icase+1, ans);
	}

	return 0;
}
