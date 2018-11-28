#include <stdio.h>
#include <string.h>

int n,L,H;
int A[200];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d%d%d",&n,&L,&H);
		for(int i=0;i<n;++i)
			scanf("%d", A+i);
		
		int ans = -1;
		for(int i=L;i<=H;++i) {
			bool find=true;
			for(int j=0;j<n;++j)
				if( A[j]%i && i%A[j] ) {
					find = false;
					break;
				}
			if(find) {
				ans = i;
				break;
			}
		}
		
		printf("Case #%d: ",++c);
		if(ans == -1)
			puts("NO");
		else 
			printf("%d\n",ans);
	}
	
	return 0;
}
