#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define FOR(i,a,n) for(int i=a,_n=n; i<_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

int main() {
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);
    int a[10005],b[10005],sw[10005];
	int tcase,n,m;
	
	scanf("%d",&tcase);
	FOR (tc, 1, tcase+1){
		scanf("%d",&n);
		FOR (i, 0, n) scanf("%d %d",&a[i],&b[i]);	
			
		scanf("%d",&a[n]);
		
		bool res=false;
		priority_queue <pair <int, int> > pq;
		memset(sw,0,sizeof(sw));
		pq.push(make_pair(0,a[0]));
		sw[0]=a[0];
		
		while (!pq.empty()) {
			int x=pq.top().first; int y=pq.top().second;
			pq.pop();

			if (y==sw[x]) {
				FOR (j, x+1, n+1) {
					if (j==n && a[x]+y>=a[n]) {res=true; break;}
					else if (j!=n && a[x]+y>=a[j]) {
						int tes=min(a[j]-a[x],b[j]);
						if (tes>sw[j]){pq.push(make_pair(j,tes)); sw[j]=tes;}
					} else break;
					if (res) break;	
				}
				if (res) break;
			}
			
			if (res) break;
		}
		
		printf("Case #%d: ",tc);
		if (res) printf("YES\n"); 
        else printf("NO\n");
		
	}
    return 0;
}
