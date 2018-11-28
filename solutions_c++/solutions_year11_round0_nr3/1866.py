#include<cstdio>
#include<cstring>
using namespace std;
const int inf=0x7fffffff;
int n,i,l,sum,t,min,x,tot;
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for(l=1;l<=t;l++){
        printf("Case #%d: ",l);
		scanf("%d",&n);
		for(i=0,tot=sum=0,min=inf;i<n;i++){
			scanf("%d",&x);
			tot+=x;
			sum^=x;
			min<?=x;
		}
		if(sum==0)printf("%d\n",tot-min);
		 else printf("NO\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
