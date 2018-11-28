#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int C,D,N,CaseNo,k=0;
	freopen("B-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&CaseNo);
	while(k++<CaseNo){
		int i,j;
		char c,temp[5];
		int opposed[26][26]={0};
		char combine[26][26]={0};
		char stack[200]={0};
		int top=0;
		scanf("%d",&C);
		for(i=0;i<C;i++){
			scanf(" %s",temp);
			combine[temp[0]-'A'][temp[1]-'A']=combine[temp[1]-'A'][temp[0]-'A']=temp[2];
		}
		scanf("%d",&D);
		for(i=0;i<D;i++){
			scanf(" %s",temp);
			opposed[temp[0]-'A'][temp[1]-'A']=opposed[temp[1]-'A'][temp[0]-'A'] = 1;
		}
		scanf("%d",&N);
		scanf(" %c",&c);
		stack[top++]=c;
		for(i=1;i<N;i++){
			scanf("%c",&c);
			stack[top++]=c;
			while((c=combine[stack[top-1]-'A'][stack[top-2]-'A'])!=0){
				stack[top-2]=c;
				top--;
				if(top == 1)
					break;
			}
			for(j=top-2;j>=0;j--)
				if(opposed[stack[j]-'A'][stack[top-1]-'A'] == 1){
					top=0;
					break;
				}
		}
		printf("Case #%d: [",k);
		if(top == 0){
			printf("]\n");
			continue;
		}
		putchar(stack[0]);
		for(j=1;j<top;j++)
			printf(", %c",stack[j]);
		printf("]\n");
	}
	return 0;
}

