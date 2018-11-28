#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a,const void *b){
	return *(int *)a - *(int *)b;
}

int main(void){
	int CaseNo,k=0;
	freopen("D-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&CaseNo);
	while(k++<CaseNo){
		int array[1000];
		int brray[1000];
		int len,i;
		double sum = 0;
		scanf("%d",&len);
		for(i=0;i<len;i++){
			scanf("%d",array+i);
			brray[i]=array[i];
		}
		qsort(array,len,sizeof(int),cmp);
		for(i=0;i<len;i++){
			if(brray[i] != array[i]){
				sum=sum+1;
			}
		}
		printf("Case #%d: %.6lf\n",k,sum);
	}
	return 0;
}
