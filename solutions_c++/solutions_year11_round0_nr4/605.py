#include <stdio.h>
#include <string.h>

int n;
int s[1010];
bool used[1010];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
			scanf("%d",s+i);
			
		memset(used,0,sizeof(used));
		int sum = 0;
		for(int i=1;i<=n;++i) {
			if(used[i])	continue;
			int size = 1;
			int ptr = s[i];
			used[i] = 1;
			while(ptr != i) {
				++size;
				used[ptr] = 1;
				ptr = s[ptr];
			}
			//printf("%d\n",size);
			if(size > 1)	sum += size;
		}
		
		printf("Case #%d: %d.000000\n",++c,sum);
	}
	
	return 0;
}
