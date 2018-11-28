#include<stdio.h>
#include<stdlib.h>
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C2.out","w",stdout);
	int T,t,n,i,o,s,a,x;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		o=0;
		a=0;
		s=1000000000;
		for(i=0;i<n;i++){
			scanf("%d",&x);
			if(x<s)s=x;
			o^=x;
			a+=x;
		}
		if(o!=0)printf("Case #%d: NO\n",t);
		else printf("Case #%d: %d\n",t,a-s);
	}
}
