#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int a,ret,sum,xo,n;

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d",&n);
		sum=0; xo=0; ret=(1<<30);
		for (int i=0; i<n; i++) {
			scanf("%d",&a);
			ret=min(a,ret);
			sum+=a;
			xo^=a;
		}
		printf("Case #%d: ",T);
		if (xo!=0) printf("NO\n");
		else {
			printf("%d\n",sum-ret);
		}
		
	}
}
