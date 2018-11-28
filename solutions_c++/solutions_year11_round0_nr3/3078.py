#include<stdio.h>
int n;
int main(){
	freopen("C:\\1\\C.in","r",stdin);
	freopen("C:\\1\\ccc.txt","w",stdout);
	int i,num;
	int T,cas=1;
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n);
		int count=0,sum=0,yihuo=0,xiao=100000000;
		for (i=1;i<=n;i++){
			scanf("%d",&num);
			sum+=num;
			yihuo^=num;
			if (num<xiao)xiao=num;
		}
		if (yihuo!=0)printf("Case #%d: NO\n",cas++);
		else printf("Case #%d: %d\n",cas++,sum-xiao);
	}
	return 0; 
}
	
