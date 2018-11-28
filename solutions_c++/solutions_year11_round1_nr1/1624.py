#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gcd(int m,int n){
	int p;
	while(m%n){
		p=m;
		m=n;
		n=p%n;
	}
	return n;
}

int main(void){
	int t,k=0;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&t);
	while(k++<t){
		int n,pd,pg,i,flag=0;
		scanf("%d%d%d",&n,&pd,&pg);
		if((pd>0&&pg==0) || (pd<100&&pg==100)){
			printf("Case #%d: Broken\n",k);
			continue;
		}
		for(i=1;i<=n;i++){
			if((i*pd)%100==0){
				flag = 1;
				break;
			}
		}
		if(flag)
			printf("Case #%d: Possible\n",k);
		else
			printf("Case #%d: Broken\n",k);
	}
	return 0;
}
