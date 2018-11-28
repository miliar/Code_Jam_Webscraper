#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <iostream>

using namespace std;

int d[105],v[105];
bool mark[105];

int main() {
int z,zz,i,j;
	freopen("d:\\in.in","r",stdin);
	freopen("d:\\out","w",stdout);
	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		int n,k,b,t,ans=0;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		int i;
		for (i=0;i<n;++i) {
			scanf("%d",&d[i]);
		}
		for (i=0;i<n;++i) {
			scanf("%d",&v[i]);
		}
		for (i=n-1;i>=0;--i) {
			if (v[i]*t+d[i]>=b) { //can
				mark[i]=true;
				for (j=i+1;j<n;++j) {
					if ((!mark[j]) && (v[i]>v[j])) { //cannot
						__int64 dv=v[i]-v[j];
						__int64 dd=d[j]-d[i];
						if (dd*v[i]+dv*d[i]-dv*b<0) {
							++ans;
						}
						
					}
				}

				--k;
				if (k<=0) {
					break;
				}

			}
			else {
				mark[i]=false;
			}
		}
		
		if (k<=0) {
			printf("Case #%d: %d\n",z,ans);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n",z,ans);
		}

	}
	return 0;
}