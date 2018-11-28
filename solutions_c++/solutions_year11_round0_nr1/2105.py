#include<cstdio>
inline int max(int A, int B){return A > B? A: B;}
inline int abs(int A){return A > 0 ? A: -A;}
int T, N, lA, lB, pA, pB;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int i = 0; i < T; i++){
		pA = pB = 1;
		lA = lB = 0;
		scanf("%d", &N);
		while(N--){
			char c[5];
			int K;
			scanf("%s%d", c, &K);
			if(c[0] == 'O'){
				lA = max(lB + 1, lA + abs(pA - K) + 1);
				pA = K;
			}else{
				lB = max(lA + 1, lB + abs(pB - K) + 1);
				pB = K;
			}
		}
		printf("Case #%d: %d\n", i + 1, max(lA, lB));
	}
}
