#include<stdio.h>
int min(int a,int b){
	return a<b?a:b;
}
int main(){
	
	int i,t;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);

	for(i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		int j,n,s,p,x,S=0,D=0;
		scanf("%d%d%d",&n,&s,&p);
		for(j=0;j<n;j++){
			scanf("%d",&x);
			if(x>=3*p-2)
				D++;
			else if(x>=3*p-4&&x>=2)
				S++;
		}
		printf("%d\n",D+min(S,s));
	}
}