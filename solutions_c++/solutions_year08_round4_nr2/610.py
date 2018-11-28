#include<stdio.h>

int main() {
	int C;
	scanf("%d", &C);
	for(int cas=1;cas<=C;cas++) {
		int x1, x2, y1, y2, N, M, A;
		scanf("%d%d%d", &N, &M, &A);
		bool succ=false;
		for(x1=0;x1<=N;x1++) {
			for(x2=0;x2<=N;x2++) {
				for(y1=0;y1<=M;y1++) {
					for(y2=0;y2<=M;y2++) {
						if((x1*y2-x2*y1)==A) {
							succ=true;
							goto end;
						}
					}
				}
			}
		}
end:	printf("Case #%d: ", cas);
		if(succ) printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
		else puts("IMPOSSIBLE");
	}
	return 0;
}