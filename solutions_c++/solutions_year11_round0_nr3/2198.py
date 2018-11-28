//

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int v[1005];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,n,tot;
	scanf("%d",&T);
	for(int Cas = 1; Cas <= T; Cas ++){
		scanf("%d",&n);
		tot = 0;
		for(int i = 0; i < n; i ++){
			scanf("%d",&v[i]);
			tot ^= v[i];
		}
		printf("Case #%d: ",Cas);
		if(tot){
			puts("NO");
		}else{
			sort(v,v+n);
			tot = 0;
			for(int i = 1; i < n; i ++){
				tot += v[i];
			}
			printf("%d\n",tot);
		}
	}
	return 0;
}