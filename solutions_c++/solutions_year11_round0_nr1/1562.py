#include <stdio.h>
#define	MAX(x, y) 	((x > y)? (x):(y))
#define	ABS(x) 	((x > 0)? (x):-(x))

int p[101];
char r[101];

int solve(){
	int i, n, time=0, dt;
	int poso=1, posb=1;
	int oi=0, bi=0;
	int to=0, tb=0;	//prepare time

	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf(" %c %d", &r[i], &p[i]);
//		printf("%c %d, ", r[i], p[i]);
	}
//	printf("\n");

	while(oi < n && r[oi]!='O')	oi++;
	while(bi < n && r[bi]!='B')	bi++;

	while(true){

		if(oi >= n && bi >= n)
			return time;

		if(oi<bi){
			dt = MAX(ABS(p[oi]-poso)-to, 0) + 1;
			time += dt;
			tb += dt;
			to = 0;
//			printf("O: dt=%4d\ttime=%d\ttb=%d\tdist=%d\n", dt, time, tb,p[oi]-poso);
			poso = p[oi];
			while(++oi < n && r[oi]!='O');
		}
		else {
			dt = MAX(ABS(p[bi]-posb)-tb, 0) + 1;
			time += dt;
			to += dt;
			tb = 0;
//			printf("B: dt=%4d\ttime=%d\tto=%d\tdist=%d\n", dt, time, to,p[bi]-posb);
			posb = p[bi];
			while(++bi < n && r[bi]!='B');
		}
	}
}

int main(){
	int i, T;
	scanf("%d", &T);

	for(i=0;i<T;i++)
		printf("Case #%d: %d\n", i+1, solve());

	return 0;
}
