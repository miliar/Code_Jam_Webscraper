#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int po, pb;
int to, tb;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A0.out", "w", stdout);
	int cas, k, ans, x, n;
	char ch;
	scanf("%d", &cas);
	for (k=1; k<=cas; k++) {
		po=1; pb=1;
		to=0; tb=0;
		ans=0;
		scanf("%d", &n);
		while (n--) {
			scanf(" %c%d", &ch, &x);
			if (ch=='O') {
				int tmp=abs(x-po)+1;
				po=x;
				if (to+tmp<=ans) ans++, to=ans;
				else {
					ans=to+tmp;
					to=ans;
				}
			}
			else if (ch=='B') {
				int tmp=abs(x-pb)+1;
				pb=x;
				if (tb+tmp<=ans) ans++, tb=ans;
				else {
					ans=tb+tmp;
					tb=ans;
				}
			}
			//printf("%d     %d %d    %d %d\n", ans, po, to, pb, tb);
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
