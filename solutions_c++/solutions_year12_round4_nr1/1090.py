#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <string>
#define INF 2000000000
#define ii pair<int, int>

using namespace std;

int a[10005],b[10005],swing[10005];

int main() {
	int ntc,n,m;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++) {
		scanf("%d",&n);
		for (int i=0;i<n;i++) {
			scanf("%d %d",&a[i],&b[i]);	
		}	
		scanf("%d",&a[n]);
		bool res=false;
		priority_queue <pair <int, int> > pq;
		memset(swing,0,sizeof(swing));
		pq.push(make_pair(0,a[0]));
		swing[0]=a[0];
		while (!pq.empty()) {
			int x=pq.top().first; int y=pq.top().second;
			pq.pop();
			//printf(">> %d %d\n",x,y);
			if (y==swing[x]) {
				for (int j=x+1;j<=n;j++) {
					if (j==n && a[x]+y>=a[n]) {res=true; break;}
					else if (j!=n && a[x]+y>=a[j]) {
						int tes=min(a[j]-a[x],b[j]);
						if (tes>swing[j]){pq.push(make_pair(j,tes)); swing[j]=tes;}
					} else break;
					if (res) break;	
				}
				if (res) break;
			}
			if (res) break;
		}
		printf("Case #%d: ",tc);
		if (res) printf("YES\n"); else printf("NO\n");
		
	}
    return 0;
}
