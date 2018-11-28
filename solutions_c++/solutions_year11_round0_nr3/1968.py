#include <stdio.h>
#include <algorithm>
using namespace std;

int val[1010];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, t, n, i, psum, ssum;
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		scanf("%d", &n);
		psum = 0;
		for(i = 0; i < n; i++){
			scanf("%d", &val[i]);
			psum^=val[i];
		}
		if(!psum){
			sort(val, val+n);
			ssum = 0;
			for(i = 1; i < n; i++) ssum += val[i];
			printf("Case #%d: %d\n", t, ssum);
		}
		else printf("Case #%d: NO\n", t);
	}
	return 0;
}
