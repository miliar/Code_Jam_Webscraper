#include<cstdio>
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		int sum=0,s=0,min=10000000;
		int x,n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf("%d",&x);
			if (x<min)min=x;
			sum^=x;
			s+=x;
		}
		printf("Case #%d: ",TT);
		if (sum!=0)printf("NO\n");
		else printf("%d\n",s-min);
	}
	
}
