#include <iostream>
#include <string.h>
using namespace std;

typedef long long int64;

int g[1000];

int vis[1000];
int64 m[1000];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int test=1;test<=t;test++) {
		int r,k,n;
		scanf("%d %d %d",&r,&k,&n);
		for (int i=0;i<n;i++) scanf("%d",&g[i]);
		int64 money=0;
		memset(vis,-1,sizeof(vis));
		int p=0;
		m[0]=0;
		vis[0]=0;
		for (int it=1;it<=r;) {
			int cap=0;
			int64 cost=0;
			int p0=p;
			while (cap+g[p]<=k) {
				cap+=g[p]; cost+=g[p]; p=(p+1)%n;
				if (p==p0) break;
			}
			money+=cost;
			if (vis[p]==-1) {
				m[p]=money;
				vis[p]=it;
				it++;
			} else {
				int cikel=it-vis[p];
				int num=(r-it)/cikel;
				money+=(money-m[p])*num;
				it+=1+num*cikel;
			}
		}
		cout << "Case #" << test << ": " << money << endl;
	}
    return 0;
}
