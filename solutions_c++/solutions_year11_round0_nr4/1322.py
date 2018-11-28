#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define maxn (10000)

int a[maxn];
int n,T;

int main(){
	scanf("%d",&T);
	
	for (int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		double ans=0.;
		for (int i=1;i<=n;i++) if (i!=a[i]) ans+=1.;
		printf("%.6lf\n",ans);
	}

	return 0;
}
