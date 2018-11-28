#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

long N,M,A;
long factors[1000];
long solX,solY;
bool done;
int factors_size;

void find(long x, long y) {
	if(done || x > N) {
		return;
	}
	if(x <= N && y <= M) {
		solX = x;
		solY = y;
		done = true;
	}
	//printf("searching for %ld, %ld\n",x,y);
	for(int i=1; i<factors_size; i++) {
		if(y % factors[i] == 0) {
	//		printf("impart y cu %ld\n", factors[i]);
			find(x*factors[i], y/factors[i]);
		}
	}
}

int factorize(long A, long &X, long &Y) {
	factors_size = 1;
	long n, newA=A;
	for(n=2; n<=newA; n++) {
		if(newA % n == 0) {
			factors[factors_size++] = n;
			while(newA % n == 0) {
				newA /= n;
			}
		}
	}/*
	printf("Factorizez %ld: ",A);
	for(int i=1; i<factors_size; i++) {
		printf("%ld ", factors[i]);
	}
	printf("\n");
	*/
	done = false;
	find(1,A);
	if(!done) {
		return 0;
	} else {
		X = solX;
		Y = solY;
		return 1;
	}
}

inline long mod(long a) {
	return a < 0 ? -a : a;
}

inline long area(int x1, int y1, int x2, int y2, int x3, int y3) {
	return mod(x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1 * y3);
}

void solve2(int case_number) {
	int x1,y1,x2,y2,a;
	for(x1=0; x1<=N; x1++) {
		for(y1=0; y1<=M; y1++) {
			for(x2=0; x2<=N; x2++) {
				for(y2=0; y2<=M; y2++) {
					a = area(x1,y1,x2,y2,0,0);
					if(a == A) {
						printf("Case #%d: %d %d %d %d %d %d\n", case_number, 0, 0, x1, y1, x2, y2);
						return;
					}
				}
			}
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", case_number);
}

void solve(int case_number) {
	long x3,y2, x2,y3;
	long newA;
	if(factorize(A, x2, y3)) {
		printf("Case #%d: %d %d %d %d %d %d\n", case_number, 0, 0, x2, 0, x2, y3);
		fprintf(stderr,"Case #%d: %d %d %d %d %d %d\n", case_number, 0, 0, x2, 0, x2, y3);
		return;
	}
	for(x3=0; x3<=N; x3++) {
		for(y2=x3; y2<=M; y2++) {
			newA = A + x3*y2;
			//printf("x3: %ld, y2: %ld, newA: %ld\n", x3, y2, newA);
			if(factorize(newA, x2, y3)) {
				printf("Case #%d: %d %d %d %d %d %d\n", case_number, 0, 0, x2, y2, x3, y3);
				fprintf(stderr,"Case #%d: %d %d %d %d %d %d\n", case_number, 0, 0, x2, y2, x3, y3);
				return;
			}
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", case_number);
	fprintf(stderr,"Case #%d: IMPOSSIBLE\n", case_number);
}

int main(void) {
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	int i, T;
	scanf("%d",&T);
	for(i=1; i<=T; i++) {
		scanf("%ld %ld %ld\n", &N, &M, &A);
		solve(i);
		//solve2(i);
		fflush(stdout);
	}

	return 0;
}