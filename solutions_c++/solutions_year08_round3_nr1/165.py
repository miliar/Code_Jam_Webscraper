#include <stdio.h>
#include <algorithm>
#include <functional>
#define MAXN 1000

using namespace std;

int main()
{
	int i, P, K, n;
	int freq[MAXN];
	int icase, ncase;
	int ans, count;
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d%d", &P, &K, &n);
		for(i=0; i<n; ++i)
			scanf("%d", &freq[i]);
		sort(freq, freq+n, greater<int>());
		ans = 0;
		for(i=0; i<n; ++i){
			ans += freq[i] * ((i/K)+1);
			if(i/K+1 > P)
				fprintf(stderr, "how could this be possible\n");
		}
		printf("Case #%d: %d\n", icase+1, ans);
	}


	return 0;
}
