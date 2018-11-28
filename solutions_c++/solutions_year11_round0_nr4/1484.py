#include<stdio.h>
int n;
int main(){
	freopen("C:\\1\\D.in","r",stdin);
	freopen("C:\\1\\ddd.txt","w",stdout);
	int i,num;
	int T,cas=1;
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n);
		int count=0;
		for (i=1;i<=n;i++){
			scanf("%d",&num);
			if (i!=num)++count;
		}
		printf("Case #%d: %f\n",cas++,count*1.0);
	}
	return 0; 
}
	
