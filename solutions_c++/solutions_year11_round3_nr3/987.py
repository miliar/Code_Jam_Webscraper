#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int t,k=0;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&t);
	while(k++<t){
		int n,l,h,i,j;
		int other[120];
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%d",other+i);
		for(i=l;i<=h;i++){
			for(j=0;j<n;j++){
				if(i%other[j]!=0&&other[j]%i!=0)
					break;
			}
			if(j==n)
				break;
		}
		printf("Case #%d: ",k);
		if(i<=h){
			printf("%d\n",i);
		}else{
			printf("NO\n");
		}
	}
	return 0;
}
