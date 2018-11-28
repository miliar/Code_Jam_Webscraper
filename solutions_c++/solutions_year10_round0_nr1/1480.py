#include <cstdio>

int n, k;

inline bool solve() {
	scanf("%d %d", &n, &k);
	return ((k+1)%(1<<n)) == 0;
}


int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %s\n", i, solve()?"ON":"OFF"); 
	
}