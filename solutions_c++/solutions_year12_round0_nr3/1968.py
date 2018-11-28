#include <cstdio>
#include <cstring>

const int N = 2000010;

int ok[N];

long long solve(int st, int ed){
	long long rn = 0;
	for (int i = st, j, k, mul, t1, t2; i <= ed; i++){
		j = i; k = 0; mul = 1;
		//printf("#%d: ", i);
		while (j){
			k = (j % 10) * mul + k;
			j /= 10;
			
			t1 = k;
			t2 = j;
			while (t2){
				t1 *= 10;
				t2 /= 10;
			}
			t1 += j;
			if (i < t1 && t1 <= ed && ok[t1]){
				rn++;
				ok[t1] = 0;
			//	printf("(%d, %d)\n", i, t1);
			}
		//	printf("%d ", t1);
			mul *= 10;
		}
		j = i; k = 0; mul = 1;
		while (j){
			k = (j % 10) * mul + k;
			j /= 10;
			
			t1 = k;
			t2 = j;
			while (t2){
				t1 *= 10;
				t2 /= 10;
			}
			t1 += j;
			if (i < t1 && t1 <= ed){
				ok[t1] = 1;
			//	printf("(%d, %d)\n", i, t1);
			}
		//	printf("%d ", t1);
			mul *= 10;
		}
	//	puts("");
		
	}
	return rn;
}

int main(){
	for (int i = 0; i < N; i++) ok[i] = 1;
	
	int nT;
	scanf("%d", &nT);
	for (int i = 1, st, ed; i <= nT; i++){
		scanf("%d %d", &st, &ed);
		printf("Case #%d: %I64d\n", i, solve(st, ed));
	}
	
	return 0;
}
