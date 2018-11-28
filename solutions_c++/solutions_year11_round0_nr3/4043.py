#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
	int cs;
	scanf("%d",&cs);
	for(int ct=1;ct<=cs;ct++){
		printf("Case #%d: ",ct);
		int n;
		scanf("%d",&n);
		unsigned arr[n];
		for(int i=0;i<n;i++)scanf("%d",&arr[i]);
		unsigned ans=0;
		for(unsigned i=1,tmp=1<<n;i<=tmp;i++){
			unsigned a=0,aa=0,b=0,bb=0;
			for(int j=0;j<n;j++){
				if((i>>j)&1){
					if(!a){
						aa=arr[j];
					}else{
						aa^=arr[j];
					}
					a+=arr[j];
				}else{
					if(!b){
						bb=arr[j];
					}else{
						bb^=arr[j];
					}
					b+=arr[j];
				}
			}
			if(a>0&&b>0&&aa==bb)ans=max(ans,max(a,b));
		}
		if(ans)
			printf("%u\n",ans);
		else puts("NO");
	}
	return 0;
}
