#include<stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;TT++){
		int n;
		scanf("%d",&n);
		int a[40]={0};
		for(int i=0;i<n;i++){
			char c[100];
			scanf("%s",c);
			for(int j=0;j<n;j++){
				if(c[j]=='1'){
					a[i]=j+1;
				}
			}
		}
		int ret=0;
		for(int i=0;i<n;i++){
			if(a[i]<=i+1){
			}else{
				for(int j=i+1;j<n;j++){
					if(a[j]<=i+1){
						int p=a[j];
						for(int k=j;k>i;k--){
							a[k]=a[k-1];
						}
						a[i]=p;
						ret+=j-i;
						break;
					}
				}
			}
		}
		/*for(int i=0;i<n;i++){
			printf("%d ",a[i]);
		}*/

		printf("Case #%d: %d\n",TT,ret);
	}
}