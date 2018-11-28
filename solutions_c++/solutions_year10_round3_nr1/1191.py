#include <cstdio>
#define min(a,b) (a < b ? a : b)
#define max(a,b) (a < b ? b : a)

int intersect(int a[2], int b[2]) {
	int A1 = a[1] - a[0];
	int B1 = 0-1;
	int C1 = B1*a[0];
	
	
	int A2 = b[1] - b[0];
	int B2 = 0-1;
	int C2 = B2*b[0];
	
	double det = A1*B2 - A2*B1;
	double x,y;
    if(det == 0){
		return 0;
    }else{
		x = (B2*C1 - B1*C2)/det;
		y = (A1*C2 - A2*C1)/det;
    }

	if (min(0,1) <= x && x <= max(0,1) && min(a[0],a[1]) <= y && y <= max(a[0],a[1]) )
		return 1;
	else return 0;
}

int main () {
	int T;
	scanf("%d", &T);
	
	
	for(int a = 1; a <= T; ++a) {
		int N;
		scanf("%d", &N);
		int lines[N][2];
		int sols = 0;
		for(int n = 0; n < N; ++n) {
			scanf("%d %d", &lines[n][0], &lines[n][1]);
		}
		
		for(int n = 0; n < N; ++n) {
			for(int x = 1+n; x < N; ++x) {
				if (intersect(lines[n], lines[x]))
					++sols;
			}
		}
		printf("Case #%d: %d\n", a, sols);
	}
}