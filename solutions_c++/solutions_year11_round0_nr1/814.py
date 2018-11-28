
#include <cstdio>
using namespace std;

char buf[8];
int n, bot[105], key[105];

int next(int b, int prg) {
	for (int i=prg; i<n; i++) if (bot[i]==b) return key[i];
	return 1;
}

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int test=1; test<=ntc; test++) {
	
		
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			scanf("%s%d",buf,key+i);
			bot[i]=buf[0]=='O'?0:1;
		}
		
		int step=0, prg=0, pos[]={1,1}, tgt[]={next(0,0),next(1,0)};
		
		while (prg<n) {
			step++;
			bool press=false;
			for (int b=0; b<2; b++) {
				if (b==bot[prg] && pos[b]==key[prg]) {
					press=true;
					tgt[b]=next(b,prg+1);
				} else {
					if (pos[b]<tgt[b]) pos[b]++;
					if (pos[b]>tgt[b]) pos[b]--;
				}
			}
			if (press) prg++;
		}
		
		printf("Case #%d: %d\n", test, step);
	}
}
