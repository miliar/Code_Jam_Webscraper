#include <stdio.h>

int T,n,l,h,t[100000];
int f;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int lT,i;
	scanf("%d",&T);
	for(lT=1;lT<=T;lT++){
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%d",&t[i]);
		for(f=l;f<=h;f++){
			for(i=0;i<n;i++)
				if(!(t[i]%f==0 || f%t[i]==0))
					break;
			if(i==n)break;
		}
		if(f<=h)printf("Case #%d: %d\n",lT, f);
		else printf("Case #%d: NO\n",lT);
	}
	return 0;
}