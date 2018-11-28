#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define maxn (10000)

int a[maxn];
int m,n,T,tot,sum;

int main(){
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		scanf("%d",&n);
		sum=tot=0; m=-1;
		for (int i=1;i<=n;i++) {
			int x; scanf("%d",&x);
			if (m==-1||m>x) m=x;
			tot^=x; sum+=x;
		}
		
		if (tot) printf("NO\n");
		else printf("%d\n",sum-m);
	}

	return 0;
}
