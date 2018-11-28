#include<stdio.h>
long min;
long t,tt,f,n,sum;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	register long a;
	scanf("%ld",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%ld",&n),min=~0U>>1,f=0,sum=0;
		while(n--) scanf("%ld",&a),min=a<min?a:min,f^=a,sum+=a;
		printf("Case #%ld: ",tt);
		if(f) puts("NO");
		else printf("%ld\n",sum-min);
		}
	scanf("%ld",&t);
	return 0;
}
