#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn=1010;
int tr,n,a[maxn];

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%d",&n);
		int sumx=0,sum=0,mint=10000000;
		for (int i=0;i<n;i++){
			scanf("%d",&a[i]);
			sumx^=a[i];
			sum+=a[i];
			mint=min(mint,a[i]);
		}
		printf("Case #%d: ",test+1);
		if (sumx) printf("NO\n");
		else printf("%d\n",sum-mint);
	}

	return 0;
}
