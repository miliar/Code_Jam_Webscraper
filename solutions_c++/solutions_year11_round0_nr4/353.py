//GoroSort
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int TST;
	scanf("%d",&TST);
	for(int tst=1;tst<=TST;++tst){
		int n;
		int a[1100],b[1100];
		scanf("%d\n",&n);
		for(int i=1;i<=n;++i) scanf("%d",&a[i]);
		memcpy(b,a,sizeof(a));
		sort(b+1,b+n+1);
		int ans=0;
		for(int i=1;i<=n;++i) ans+=(a[i]!=b[i]);
		printf("Case #%d: ",tst);
		printf("%d\n",ans);
	}
}
