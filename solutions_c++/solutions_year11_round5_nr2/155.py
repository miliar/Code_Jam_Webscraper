#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;

int tc;
int n,a[1005],ret=0,ok;
priority_queue<pair<int,int> > q;

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		ret=0;
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%d",&a[i]);
		sort(a,a+n);
		int ind,cnt;
		for (int k=1; k<=n; k++) {
			ok=1;
			//printf("%d %d\n",k,ret);
			for (int i=0; i<n; i++) {
				while (!q.empty() && -q.top().first+1<a[i] && -q.top().second>=k) q.pop();
				if (q.empty()) q.push(make_pair(-a[i],-1));
				else {
					ind=-q.top().first;
					cnt=-q.top().second;
					//printf("  %d - %d %d\n",a[i],ind,cnt);
					
					if (ind+1<a[i]) {
						ok=0; break;
					}
					if (ind+1==a[i]) {
						q.pop();
						q.push(make_pair(-a[i],-cnt-1));
						continue;
					}
					q.push(make_pair(-a[i],-1));
				}
			}
			while (!q.empty() && -q.top().second>=k) q.pop();
			if (ok==1 && q.empty()) ret=max(ret,k);
			while (!q.empty()) q.pop();
		}
		printf("Case #%d: %d\n",T,ret);
	}
}
