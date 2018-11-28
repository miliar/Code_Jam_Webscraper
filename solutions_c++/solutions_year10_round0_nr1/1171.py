#include <stdio.h>

int t,n,k,ex;

int main() {
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);

scanf("%d",&t);

for (int ct=0;ct<t;ct++) {
	printf("Case #%d: ",ct+1);
        scanf("%d%d",&n,&k);
	ex=1 << n;
	k%=ex;
	if ((k+1)==ex) printf("ON\n");else printf("OFF\n");
	}

return 0;
}
