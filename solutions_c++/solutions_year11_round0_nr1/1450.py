#include<cstdio>
#include<cstdlib>

int main() {
	int oTime, bTime, ans, oPos, bPos, pos, n, t;
	char col;
	freopen("A-large.in", "r", stdin);
	freopen("OutLargeA.txt", "w", stdout);
	
	scanf("%d", &t);
	fprintf(stderr, "%d\n", t);
	for(int kase = 1; kase <= t; ++kase) {
		scanf("%d", &n);
		oTime = bTime = 0;
		oPos = bPos = 1;
		
		while(n--) {
			scanf(" %c %d", &col, &pos);
			if(col == 'O') {
				oTime += abs(pos - oPos) + 1;
				oPos = pos;
				if(oTime <= bTime) oTime = bTime + 1;
			} else {
				bTime += abs(pos - bPos) + 1;
				bPos = pos;
				if(bTime <= oTime) bTime = oTime + 1;
			}
		}
		if(oTime > bTime)
			ans = oTime;
		else
			ans = bTime;
		printf("Case #%d: %d\n", kase, ans);
	}
}
