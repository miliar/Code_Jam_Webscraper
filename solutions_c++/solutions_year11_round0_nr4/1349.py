#include <cstdio>
using namespace std;

int n,N,k;
double ans;

int main() {
	scanf("%d",&N);
	for (int I=1;I<=N;I++) {
		scanf("%d",&n);
		ans=0;
		for (int i=1;i<=n;i++) {
			scanf("%d",&k);
			if (i!=k) ans=ans+1;
		}
		printf("Case #%d: %0.6lf\n",I,ans);
	}
}
