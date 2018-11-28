
#include <cstdio>
#include <cstdlib>

int myabs(int x){
	if(x < 0) return -x;
	return x;
}

int main(){
	
	int t; scanf("%d", &t);
	char c[1000];
	char buf[100];
	int p[1000];
	int h[1000];

	for(int x=1; x<=t; ++x){
		int n; scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%s %d", buf, &p[i]);
			c[i] = buf[0];
		}
		int ap, bp;
		int at, bt;

		ap = bp = 1;
		at = bt = 0;

		for(int i=0; i<n; ++i){
			int tmp;
			if(c[i] == 'O'){
				tmp = at + myabs(p[i]-ap) + 1;
			}else{
				tmp = bt + myabs(p[i]-bp) + 1;
			}
			if(i > 0 && tmp <= h[i-1]){
				tmp = h[i-1]+1;
			}
			h[i] = tmp;
			if(c[i] == 'O'){
				at = tmp; ap = p[i];
			}else{
				bt = tmp; bp = p[i];
			}
		}
		printf("Case #%d: %d\n", x, h[n-1]);
	}
	return 0;
}
