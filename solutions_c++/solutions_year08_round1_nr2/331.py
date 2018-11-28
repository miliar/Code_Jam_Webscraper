#include<stdio.h>

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		int N, M;
		scanf("%d%d", &N, &M);
		int mask=(1<<N)-1;
		int custom[100][2];
		for(int i=0;i<M;i++) {
			int c0=0, c1=0;
			int t;
			scanf("%d", &t);
			for(int j=0;j<t;j++) {
				int x, y;
				scanf("%d%d", &x, &y);
				x--;
				if(y==0) c0|=(1<<x);
				else c1|=(1<<x);
			}
			custom[i][0]=c0;
			custom[i][1]=c1;
		}
		int res=-1;
		for(int i=0;i<(1<<N);i++) {
			bool succ=true;
			for(int j=0;j<M;j++) {
				int um=custom[j][0]&(~i)&mask;
				int me=custom[j][1]&i&mask;
				if(!(um||me)) {
					succ=false;
					break;
				}
			}
			if(succ) {
				res=i;
				break;
			}
		}
		printf("Case #%d:", cas);
		if(res==-1) puts(" IMPOSSIBLE");
		else {
			for(int i=1, c=0;c<N;c++, i<<=1) {
				if(i&res) printf(" 1");
				else printf(" 0");
			}
			putchar('\n');
		}
	}
	return 0;
}