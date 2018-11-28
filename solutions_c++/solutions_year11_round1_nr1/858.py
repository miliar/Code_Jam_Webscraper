#include<cstdio>
#include<cstring>
using namespace std;
#define LL long long

int main(){
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	
	int t,cas=0;
	scanf("%d",&t);
	while(t--){
		 LL n;
		 int pd,pg;
		 scanf("%lld %d%d",&n,&pd,&pg);
		 printf("Case #%d: ",++cas);
		 if(n<100){
		 	bool flag=false;
			if(pd!=100&&pg==100) flag=false;
			else if(pd!=0&&pg==0) flag=false;
			else{
			 	for(int i=1;i<=n;i++){
			 		if((i*pd)%100==0){
						flag=true;
			 			break;
					}
			 	}
			}
		 	puts(flag?"Possible":"Broken");
		 }else{
		 	bool flag=true;
		 	if(pd!=100&&pg==100) flag=false;
		 	else if(pd!=0&&pg==0) flag=false;
		 	puts(flag?"Possible":"Broken");
		 }
	}
}