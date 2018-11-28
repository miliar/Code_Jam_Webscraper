//google code jam qualification
#include <stdio.h>

const int maxn=1024;

int n;
long ci[maxn];

void inputData(){
	scanf("%d", &n);
	for (int i=0; i<n; i++)
		scanf("%ld", &ci[i]);
}

int main(){
	int caseT, caseIndex;
	scanf("%d", &caseT);
	for (caseIndex=1; caseIndex<=caseT; caseIndex++){
		inputData();
		long result=0, sum=0, min=ci[0];
		for (int i=0; i<n; i++){
			result=result^ci[i];
			sum+=ci[i];
			if (ci[i]<min) min=ci[i];
		}

		printf("Case #%d: ", caseIndex);
		if (result==0){
			printf("%ld", sum-min);
		}else printf("NO");
		printf("\r\n");
	}

	return 0;
}