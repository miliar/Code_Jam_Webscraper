#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define FOREACH(it, v) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)

using namespace std;

int costs[1000][1000];
int miss[10000];

int main() {
	int T, P, ans;
	
	scanf("%d\n", &T);
	
	FOR(nCase, T) {
		scanf("%d\n", &P);
		
		for(int i = 0; i < 1<<P; i++) {
			scanf("%d ", &miss[i]);
			miss[i] = P - miss[i];
		}
		
		FOR(i, P) {
			for(int j = 0; j < 1<<(P-i-1); j++) {
				scanf("%d ", &costs[0][0]);
			}
		}
		
		ans = 0;
		
		for(int i = P-1; i >= 0; i--) {
			for(int j = 0; j < 1<<(P-i-1); j++) {
				bool buy = false;
				for(int k = 0; k < 1<<P; k++) {
					if((k & ~((1 << (i+1)) - 1)) == (j << (i+1))) {
						if(miss[k] > 0) buy = true;
					}
				}
				
				if(buy) {
					ans++;
					for(int k = 0; k < 1<<P; k++) {
						if((k & ~((1 << (i+1)) - 1)) == (j << (i+1))) {
							miss[k]--;
						}
					}
				}
			}
		}
		
		printf("Case #%d: %d\n", nCase+1, ans);
	}
}
