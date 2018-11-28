#include <cstdio>

using namespace std;

int tr,n;

int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%d",&n);
		int ans=0;
		for (int i=1;i<=n;i++){
			int a;
			scanf("%d",&a);
			if (a!=i) ans++;
		}
		printf("Case #%d: %d.000000\n",test+1,ans);
	}

	return 0;
}
