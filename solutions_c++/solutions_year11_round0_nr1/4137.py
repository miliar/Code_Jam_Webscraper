#include <cstdio>
#include <cstdlib>
#include <cmath>

#define abs(a) ((a)>0?(a):-(a))

int t, n, b[1000], la, lb, ta, tb, cu, ct;
char c[1000], tmp;

int main(void){
	scanf("%d", &t);
	for(int k=0; k<t; k++){
		scanf("%d", &n);
		for(int i=0; i<n; i++){scanf("%c%c%d", &tmp, &c[i], &b[i]);}
		ta = tb = cu = 0;
		la = lb = 1;
		for(int i=0; i<n; i++){
			if(c[i]=='O'){
				cu++;
				if(cu-ta<abs(b[i]-la) + 1) cu = abs(b[i]-la) + ta + 1;
				la = b[i];
				ta = cu;
			}
			if(c[i]=='B'){
				cu++;
				if(cu-tb<abs(b[i]-lb) + 1) cu = abs(b[i]-lb) + tb + 1;
				lb = b[i];
				tb = cu;
			}
		}
		printf("Case #%d: %d\n", k+1, cu);
	}
	return 0;
}
