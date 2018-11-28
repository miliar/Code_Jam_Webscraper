#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

bool pure[500];

int backtrack(int i, int rank, int n) {
	if(i == n) return pure[rank];
	
	int ans = 0;
	pure[i] = pure[rank];
	ans += backtrack(i+1, rank+1, n);
	pure[i] = false;
	
	ans += backtrack(i+1, rank, n);
	
	return ans;
}

int main() {
	int T, n;
	
	scanf("%d\n", &T);
	
	FOR(nCase, T) {
		scanf("%d\n", &n);
		
		pure[1] = true;
		printf("Case #%d: %d\n", nCase+1, backtrack(2, 1, n)%100003);
	}
}
