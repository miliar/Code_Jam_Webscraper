#include<stdio.h>
int main(){
	int _,n,x;
	scanf("%d",&_);
	for(int t=1; t<=_; t++){
		scanf("%d",&n);
		int ans=0;
		for(int i=1; i<=n; i++)
		{
			scanf("%d",&x);
			if(x!=i)ans++;
		}
		printf("Case #%d: %d.000000\n",t,ans);
	}
	return 0;
}
