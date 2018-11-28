//dancing.cpp
//By λKT345

#include<cstdio>

int T, N, S, P;

int main() {
	int sco, tot, cur, mod;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		scanf("%d%d%d", &N, &S, &P);
		tot=0;
		for(int i=1; i<=N; i++) {
			scanf("%d", &sco);
			cur=sco/3;
			mod=sco%3;
			if(cur>=P) {
				tot++;
			} else if(mod==0) {
				if(cur+1>=P&&cur-1>=0&&S>0) {
					tot++;
					S--;
				}
			} else if(mod==1) {
				if(cur+1>=P) {
					tot++;
				}
			} else {
				if(cur+2>=P&&S>0){
					tot++;
					S--;
				} else if(cur+1>=P){
					tot++;
				}
			}
		}
		printf("Case #%d: %d\n", t, tot);
	}
	return 0;
}
