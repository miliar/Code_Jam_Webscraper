#include <cstdio>
int TC,n,k,AC;
int main(){
	scanf("%d",&TC);
	for (int C=1;C<=TC;C++){
		scanf("%d%d",&n,&k);
		if (!k) AC=0;
		else {
			if ((k+1)%(1<<n)==0) AC=1; else AC=0;
		}
		printf("Case #%d: %s\n",C,AC==0?"OFF":"ON");
	}	
	scanf("\n");
	return 0;
}
