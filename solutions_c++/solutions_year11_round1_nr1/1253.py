#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int main(){
	
	int casos; scanf("%d", &casos);
	int caso = 1;
	int pd, pg, n;
	while(casos--){
		printf("Case #%d: ", caso++);
		scanf("%d%d%d", &n, &pd, &pg);
		if(pg == 100 && pd != 100 || pg == 0 && pd != 0) {
			printf("Broken\n");
		}else{
			int gc = __gcd(pd, 100);
			if(100/gc > n) {
				printf("Broken\n");
				continue;
			}
			
			printf("Possible\n");
		}
	}
	
	return 0;
}