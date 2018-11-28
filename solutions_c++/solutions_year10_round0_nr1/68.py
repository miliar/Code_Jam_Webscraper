#include<stdio.h>
int main(){
	int times,n,k;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		scanf("%d%d",&n,&k);
		bool ans=true;
		for(int i=0;i<n;i++){
			if(!(k & (1<<(i)))){
				ans=false;
				break;
			}
		}
		printf("%s\n",ans ?"ON":"OFF");
	}
	return 0;
}
