#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#define S 50000

int T;
int x,n;
long long l,f[S+11],ans,a[222];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		memset(f,63,sizeof(f));
		scanf("%I64d %d",&l,&n);
		f[0]=0;
		for(int i=0;i<n;i++){
			scanf("%d",&x);
			a[i]=x;
			for(int j=x;j<=S;j++) f[j]<?=f[j-x]+1;
		}
		ans=(long long)2e18;
		for(int i=0;i<=S;i++)
			for(int j=0;j<n;j++)
				if(!((l-i)%a[j]))
					ans<?=f[i]+(l-i)/a[j];
		printf("Case #%d: ",_);
		if(ans>=2e18) puts("IMPOSSIBLE");else printf("%I64d\n",ans);
	}
	return 0;
}
