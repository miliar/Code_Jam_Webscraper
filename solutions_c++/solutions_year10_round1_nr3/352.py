#include <cstdio>
#include <cstdlib>

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)

bool check(int a, int b){
	if(a == b) return false;
	if(a % b == 0 || b % a == 0) return true;
	if(abs(a - b) == 1) return false;
	for(int k = (b - 1) / a; k; k--) if(!check(a, b - a * k)) return true;
	for(int k = (a - 1) / b; k; k--) if(!check(b, a - b * k)) return true;
	return false;
}

int main(){
	int T;
	scanf("%d ", &T);
	for(int i = 1; i <= T; i++){
		int A1, A2, B1, B2;
		scanf("%d %d %d %d ", &A1, &A2, &B1, &B2);
		long long count = 0;
		FOR(a, A1, A2 + 1) FOR(b, B1, B2 + 1) count += check(a, b);
		printf("Case #%d: %lld\n", i, count);
	}
	return 0;
}
