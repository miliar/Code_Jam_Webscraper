#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int soma(int a, int b) {
	int r = 0;
	for (int i=0; i < 31; ++i) {
		if ( ((a>>i)&1) && ((b>>i)&1) ) continue;
		if ( ((a>>i)&1) || ((b>>i)&1) ) {
			r += (1<<i);
		}
	}
	return r;
}

int n, v[1010], s, cn, tot, menor;
int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d",&n);
		s=0;
		tot=0;
		menor=0x60606060;
		for (int i=0; i < n; ++i) {
			scanf("%d",&v[i]);
			s = soma(s, v[i]);
			tot += v[i];
			menor = min(menor, v[i]);
		}
		
		printf("Case #%d: ",++cn);
		if (s) printf("NO\n");
		else printf("%d\n",tot-menor);
	}
	return 0;
}
