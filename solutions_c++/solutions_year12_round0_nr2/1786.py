#include<stdio.h>
int main(){
	int _,t,n,s,p,x;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d%d",&n,&s,&p);
		int ans=0,w=0;
		for(int i=0; i<n; i++){
			scanf("%d",&x);
			if(x>=3*p-2)ans++;else
			if(x>=p*3-4 && p>=2)w++;
		}
		printf("Case #%d: %d\n",t,ans+(w<s?w:s));
	}
	return 0;
}
