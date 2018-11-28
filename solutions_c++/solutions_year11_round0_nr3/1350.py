#include <cstdio>
using namespace std;

int n,N,k;

int main() {
	scanf("%d",&N);
	for (int I=1;I<=N;I++) {
		scanf("%d",&n);
		int sum=0,x=0,min=1000000000;
		for (int i=0;i<n;i++) {
			scanf("%d",&k);
			x=x^k;
			sum=sum+k;
			if (k<min) min=k;
		}
		if (x!=0) printf("Case #%d: NO\n",I); else printf("Case #%d: %d\n",I,sum-min);
	}
}
