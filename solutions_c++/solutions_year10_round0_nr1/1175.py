#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int n, k, tc;

int main() {
	scanf("%d", &tc);
	//freopen("a.out", "w", stdout);
	for(int i=1; i<=tc; i++){
		scanf("%d%d", &n, &k);
		if( k % (1 << n) == (1 << n) - 1){
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}

