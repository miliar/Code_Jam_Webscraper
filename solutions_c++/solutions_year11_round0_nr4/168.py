#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int n,a[1005],v[1005];
double ret=0;

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d",&n);
		ret=0;
		for (int i=1; i<=n; i++) scanf("%d",&a[i]);
		memset(v,0,sizeof(v));
		for (int i=1; i<=n; i++) {
			if (a[i]!=i) {
				int cnt=0,at=i;
				while (v[at]==0) {
					v[at]=1;
					at=a[at];
					cnt++;
				}
				ret+=cnt;
			}
		}
		printf("Case #%d: %f\n",T,ret);
	}
}
