#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main() {
	int cases, t = 1;
	int n, k, i, nro, now, count;
	int deck[5005], used[5005];
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d",&n);
		
		memset(used,0,sizeof(used));
		for (i=0,now=count=1; now <= n; i=(i+1)%n) {
			while (i < n && used[i]) i++;
			if (i == n) continue;
			if (count == now) {
				deck[i] = now++;
				used[i] = 1;
				count = 1;
			}
			else
				count++;
		}
		
		printf("Case #%d:",t++);
		scanf("%d",&k);
		for (i=0; i < k; i++) {
			scanf("%d",&nro);
			printf(" %d",deck[nro-1]);
		}
		puts("");
	}
	
	return 0;
}
