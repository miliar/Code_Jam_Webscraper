#include <stdio.h>


long long t,r,k,n,i,j,tn,nal,gn;
long long g[1000];
long long cst[1000],pos[1000];


int main()

{

freopen("B.in","r",stdin);
freopen("B.out","w",stdout);

scanf("%d",&t);

for (int ct=1;ct<=t;ct++) {
	printf("Case #%d: ",ct);
	scanf("%d%d%d",&r,&k,&n);
	for (i=0;i<n;i++) {
		scanf("%d",&g[i]);
		}
	for (i=0;i<n;i++) {
		j=i;
		tn=0;
		while ((tn+g[j])<=k) {
			tn+=g[j];
			j++;
			j%=n;
			if (j==i) break;
			}
		pos[i]=j;
		cst[i]=tn;
		}	
	tn=0;
	nal=0;
	
	while (r>0) {
		nal+=cst[tn];
		tn=pos[tn];
		r--;
		}
	
	printf("%I64d\n",nal);
	}

return 0;
}
