#include<stdio.h>
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int T,n,i,t,s,p,x,y,ans,w;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		ans=0;
		w=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++){
			scanf("%d",&x);
			y=x%3;
			x/=3;
			if(x>=p)ans++;
			else if(x==p-1&&y==2)ans++;
			else if(x==p-1&&y==1)ans++;
			else if(p-2<0);
			else if(x==p-1&&y==1&&s>0){ans++;s--;}
			else if(x==p-1&&y==0&&s>0){ans++;s--;}
			else if(x==p-2&&s>0&&y==2){ans++;s--;}
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
