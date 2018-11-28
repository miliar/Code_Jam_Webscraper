#include <cstdio>
#include <cstring>
#include <algorithm>
#pragma comment(linker,"/STACK:10000000")
using namespace std;
typedef long long ll;
int t,ii;
int A1,A2,B1,B2;
ll ans;
bool win(int a, int b) {
	if (a==b) return 0;
	if (a<b) swap(a,b);
	if (a%b==0) return 1;
	if (a/b>1) return 1; else return !win(b,a%b);
}
int main() {
	int i,j;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		ans=0;
		for (i=A1; i<=A2; ++i)
			for (j=B1; j<=B2; ++j)
				if (win(i,j)) ++ans;
		printf("%I64Ld\n",ans);
	}
	return 0;
}