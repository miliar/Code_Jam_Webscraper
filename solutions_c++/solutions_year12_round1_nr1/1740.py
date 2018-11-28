#include<stdio.h>

bool check(int outcomes, int back, int A){
	for(int i = A; i > 0 && back > 0; i--, back--){
		outcomes &= (1<<(i-1)) - 1;
	}
	return outcomes > 0;
}

int main(){
	int T, A, B, tc = 1;
	for(scanf("%d", &T); T; T--){
		scanf("%d %d", &A, &B);
		double p[A];
		for(int i = 0; i < A; i++)
			scanf("%lf", &p[i]);
		double P[8], E[2+A];
		for(int i = 0; i <= (1<<A) - 1; i++){
			P[i] = 1;
			for(int j = 0; j < A; j++)
				P[i] *= (i & (1 << j))? (1-p[j]) : p[j];
		}
		double min = 9000000;
		for(int i = 0; i < 2+A; i++){
			E[i] = 0;
			for(int j = 0; j <= (1<<A) - 1; j++){
				double n = 0;
				if(i == 2+A-1){
					n = 1 + B + 1;
					E[i] += n*P[j];
					continue;
				}
				n = i + (B - (A - i)) + 1;
				if(check(j, i, A))
					n += B + 1;
				E[i] += n*P[j];
			}
			if(min > E[i]) min = E[i];
		}
		printf("Case #%d: %.6lf\n", tc++, min);
	}
	return 0;
}
