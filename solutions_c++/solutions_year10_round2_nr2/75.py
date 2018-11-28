#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int x[10000], v[10000];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for(int i=0; i<n; ++i) scanf("%d", &x[i]);
		for(int i=0; i<n; ++i) scanf("%d", &v[i]);
		int res = 0, ile = 0;
		for(int i=n-1; i>=0; --i){
			if(v[i] * t >= b - x[i]) ile++;
			else{
				res += max(0, k-ile);
			}
		}
		printf("Case #%d: ", iii);
		if(ile >= k) printf("%d\n", res);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
