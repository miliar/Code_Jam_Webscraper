#include <stdio.h>

int main(){
	int cas,x,n,k,i;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cas);
	for (x=1; x<=cas; x++){
		scanf("%d%d",&n,&k);
		for (i=0; i<n; i++){
			if (k%2==0) break;
			k /= 2;
		}
		printf("Case #%d: ",x);
		if (i!=n) printf("OFF\n");
		else printf("ON\n");
	}
	return 0;
}