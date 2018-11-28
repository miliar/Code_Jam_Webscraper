#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int t;
	int n,s,p;
	int num[100];
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d%d",&n,&s,&p);
		for(int j=0;j<n;j++)
			scanf("%d",&num[j]);
		int count=0;
		int ans=0;
//		printf("%d\n",n);
		for(int j=0;j<n;j++){
			if((3*p-num[j]>2&&3*p-num[j]<=4)&&num[j]>1)
				count++;
			else if(3*p-num[j]<=2)
				ans++;
			
//		printf("%d %d\n",ans,count);
		}
//		printf("%d %d\n",ans,count);
		if(count > s)
			ans +=s;
		else
			ans +=count;
	printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
