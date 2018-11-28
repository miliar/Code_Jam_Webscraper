#include <stdio.h>
#include <string.h>
int main(){
	int i,j,k;
	int sum,v,minv;
	int tn,cp;
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		int n;
		scanf("%d",&n);
		sum=v=0;
		minv=10000000;
		for (i=0;i<n;i++){
			scanf("%d",&k);
			v^=k;
			sum+=k;
			if (k<minv) minv=k;
		}
		printf("Case #%d: ",cp);
		if (v==0){
			printf("%d\n",sum-minv);
		}else printf("NO\n");
	}
	return 0;
}
