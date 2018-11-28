#include <stdio.h>
struct instruction {
	int r;
	int button;
};
struct instruction ins[11];
int n, t;
int main() {
	scanf("%d\n", &t);
	int te=0;
	int r, p;
	while(te++<t) {
		scanf("%d ", &n);
		int alce=0;
		while(alce<n) {
			char c;
			scanf("%c %d ", &c, &p);
			if(c == 'O') r = 0;
			else r = 1;
			ins[alce].r = r;
			ins[alce].button = p;
			alce++;
		}
		int step[] = {1, 1}, time = 0;
		for(int i=0; i<n; i++) {
			int k=i;
			while(k++<n)
				if(ins[k].r != ins[i].r) break;
			while(ins[i].button) {
				time++;
				if(step[ins[i].r] == ins[i].button)
					ins[i].button = 0;
				else {
					if(step[ins[i].r]<ins[i].button)
						step[ins[i].r]++;
					else
						step[ins[i].r]--;
				}
				if(ins[k].r != ins[i].r &&step[ins[k].r] != ins[k].button) {
					if(step[ins[k].r]<ins[k].button)
						step[ins[k].r]++;
					else
						step[ins[k].r]--;
				}
			}
		}
		printf("Case #%d: %d\n", te, time);
	}
}



