//Candy Splitting
#include <cstdio>
#include <cstring>

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int TST;
	scanf("%d",&TST);
	for(int tst=1;tst<=TST;++tst){
		int n;
		scanf("%d\n",&n);
		int min=0x3f3f3f3f,a,sum=0,xr=0;
		for(int i=1;i<=n;++i){
			scanf("%d",&a);
			xr^=a;
			sum+=a;
			min=min<a?min:a;
		}
		printf("Case #%d: ",tst);
		if(xr) printf("NO\n");
		else printf("%d\n",sum-min);
	}
}
