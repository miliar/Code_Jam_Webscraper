#include <stdio.h>
#include <algorithm>
using namespace std;

#define INF 1023456789

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int t=1;t<=datasuu;t++){
		printf("Case #%d: ",t);

		int n;
		scanf("%d",&n);
		int p[1010];
		for(int i=0;i<n;i++){
			scanf("%d",&p[i]);
			p[i]--;
		}
		
		int ans=n;
		for(int i=0;i<n;i++){
			if(p[i]==i)ans--;
		}
		printf("%d.000000\n",ans);
	}
}