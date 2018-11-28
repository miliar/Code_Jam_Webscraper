#include <stdio.h>

int t,n,s,p;
int cnt;

int main() {
	scanf("%d", &t);

	for (int i=0; i<t; i++) {
		scanf("%d %d %d", &n,&s,&p);
		int sc; cnt=0;

		for (int j=0; j<n; j++) {
			scanf("%d", &sc);
			if (p==0) {
				cnt++;
				continue;
			}		
	
			if ((p-1>=0) && sc>=(2*(p-1)+p)) cnt++;
			else if ((p-2)>=0 && sc>=(2*(p-2)+p) && s) cnt++, s--;	
		}

		printf("Case #%d: %d\n", i+1,cnt);
	}

	return 0;
}
