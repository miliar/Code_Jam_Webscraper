#include<cstdio>
#define min(x,y) (((x)<(y))?(x):(y))

int t,n,s,p,a[200],cur[200],ch[200];

int main(){
	scanf("%d",&t);
	for (int tt=1;tt<=t;++tt){
		int ans=0,ok=0;
		scanf("%d%d%d",&n,&s,&p);
		for (int i=0;i<n;++i){
			scanf("%d",&a[i]);
			if (a[i]%3 != 1){
      			cur[i]=(a[i]+1)/3;
      			ch[i]=cur[i]+1;
			}
			else cur[i]=ch[i]=a[i]/3 +1;
			//printf("%d %d %d!!\n",a[i],cur[i],ch[i]);
			if (cur[i]>=p) ++ans;
			else{
				 if (a[i]>=2 && a[i]<=28 && ch[i]>=p) ++ok;
		 	}
		}
		printf("Case #%d: %d\n",tt,ans+min(s,ok));
	}
	return 0;
}
