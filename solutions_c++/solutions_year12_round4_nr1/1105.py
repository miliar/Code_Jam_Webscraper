#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAX = 10000;

int n, d[MAX+1], l[MAX], mx[MAX];


int main()
{
	int T; scanf("%d", &T);
	for (int t=1; t<=T; ++t) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &d[n]);
		
		memset(mx, 0, sizeof mx);
		mx[0] = 2*d[0];
		
		int last = 0;
		for (int i=0; i<n; ++i) {
			if (mx[i] >= d[n]) { printf("Case #%d: YES\n", t); goto end; }
			while (last<n && d[last+1] <= mx[i]) {
				++last;
				mx[last] = min(d[last]-d[i], l[last]) + d[last];
			}
		}
		
		printf("Case #%d: NO\n", t);
		end:;
	}
	
	return 0;
}
