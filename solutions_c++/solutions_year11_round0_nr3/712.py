#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int CaseNo,k=0;
	int candy[1000];
	freopen("C-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&CaseNo);
	while(k++<CaseNo){
		int t,i;
		int result=0;
		int sum = 0;
		int min = 1000006;
		scanf("%d",&t);
		for(i=0;i<t;i++){
			scanf("%d",candy+i);
			result = result^candy[i];
			sum += candy[i];
		}
		printf("Case #%d: ",k);
		if(result!=0){
			printf("NO\n");
			continue;
		}
		for(i=0;i<t;i++){
			if(min>candy[i])
				min = candy[i];
		}
		printf("%d\n",sum-min);
	}
	return 0;
}

