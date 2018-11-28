#include <cstdio>


int c, p, tc, r, k, n, i, t[1010];
int in,out,st;
int main() {

	scanf("%d",&tc);
	c = 1;
	while(c<=tc) {
		scanf("%d %d %d", &r, &k, &n);
		for(i=0;i<n;i++) scanf("%d", &t[i]);

		in = t[0];
		out = 0;
		p = 1%n;
		st = 0;
//		r--;
		while(r--) {
			while (in + t[p] <= k && (p != st)) {
				in += t[p];
				p = (p+1)%n;
			}
			out += in;
			in = t[p];
			st = p;
			p = (p+1)%n;
		}

		printf("Case #%d: %d\n",c,out);
		c++;
	}
	return 0;
}
