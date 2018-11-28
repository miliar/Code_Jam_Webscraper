#include<stdio.h>
#include<algorithm>
using namespace std;
int w[99],lw;
int main(){
	int _,t,i,j,x,ans,s,e,k,l,dig[9],now;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d",&s,&e);
		ans=0;
		for(i=s; i<=e; i++){
			l=0;
			for(x=i; x; x/=10)
				dig[l++]=x%10;
			lw=0;
			for(j=1; j<l; j++){
				if(dig[l-1-j]==0)continue;
				now=0;
				for(k=0; k<l; k++)
					now=now*10+dig[(l+l-1-j-k)%l];
				if(now>i && now<=e)
					w[lw++]=now;
			}
			sort(w,w+lw);
			ans+=unique(w,w+lw)-w;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
