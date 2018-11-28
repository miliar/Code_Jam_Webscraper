#include<iostream>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	int a,b,c;
	int flag;
	while(scanf("%d",&n)!=EOF){
		for(i=1;i<=n;i++){
			scanf("%d%d",&a,&b);
			c=1;
			c=1<<a;
			b%=c;
			if(b==c-1)printf("Case #%d: ON\n",i);
			else printf("Case #%d: OFF\n",i);
		
		
		}
	}
	return 0;
}
				


