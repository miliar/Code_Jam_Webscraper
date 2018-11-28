#include<stdio.h>
#include<queue>
#include<algorithm>
using namespace std;

int a[1024];
int n;
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > pq;

int cal(int m) {
	int ret=n;
	for(int i=0;i<n;i++) {
		while(!pq.empty()) {
			int last=pq.top().first,len=pq.top().second;
			pq.pop();
			if (last<a[i]-1) {
				if (len<ret) ret=len;
			} else if (last==a[i]-1) {
				pq.push(make_pair(a[i],len+1));
				break;
			} else {
				pq.push(make_pair(last,len));
				pq.push(make_pair(a[i],1));
				break;
			}
		}
		if (pq.empty()) pq.push(make_pair(a[i],1));
	}
	while(!pq.empty()) {
		int len=pq.top().second;
		if (len<ret) ret=len;
		pq.pop();
	}
	return ret;
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) {
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		sort(a,a+n);
		printf("Case #%d: %d\n",++cs,cal(0));
	}
	return 0;
}
