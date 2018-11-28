#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define len 105
int O[len],B[len],order[len];
char s[2];
int main(void){
	//freopen("A-small-attempt.in","r",stdin);
	//freopen("Bot Trust.out","w",stdout);
	int n,i,j,num,x,k1,k2,ak1,ak2,step,p1,p2,tem;
	while(scanf("%d",&n)==1){
		for(i=1;i<=n;i++){
			//input
			scanf("%d",&num);
			for(j=ak1=ak2=0;j<num;j++){
				scanf("%s%d",s,&x);
				if(s[0]=='O'){
					O[ak2++]=x;
					order[j]=0;
				}
				else{
					B[ak1++]=x;
					order[j]=1;
				}
			}
			//deal
			for(j=step=k1=k2=0,p1=p2=1;j<num;j++){
				if(order[j]){
					tem=abs(B[k1]-p1)+1;
					step+=tem;
					p1=B[k1++];
					if(k2<ak2)
						if(abs(O[k2]-p2)>tem){
							if(p2<=O[k2])
								p2+=tem;
							else
								p2-=tem;
						}
						else
							p2=O[k2];
				}
				else{
					tem=abs(O[k2]-p2)+1;
					step+=tem;
					p2=O[k2++];
					if(k1<ak1)
						if(abs(B[k1]-p1)>tem){
							if(p1<=B[k1])
								p1+=tem;
							else
								p1-=tem;
						}
						else
							p1=B[k1];
				}
			}
			printf("Case #%d: %d\n",i,step);
		}
	}
	return 0;
}