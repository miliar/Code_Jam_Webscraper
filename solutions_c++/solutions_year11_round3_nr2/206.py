#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

const int maxn=1000005;

struct Node {
	long long a,b;
	bool flag;
} node[maxn];

long long L,t,n,C;

bool cmp(const Node &n1,const Node &n2) {
	return n1.b>n2.b;
}

void solve() {
	int i;
	long long sum=0;
	for (i=0;i<n;i++) {
		sum+=node[i].a;
		if (sum>=t) break;
	}
	for (int j=0;j<i;j++) {
		node[j].b=0;
		node[j].flag=false;
	}
	node[i].b=(sum-t)/2;
	node[i].flag=true;
	for (int j=i+1;j<n;j++) {
		node[j].b=node[j].a/2;
		node[j].flag=false;
	}

//for (int i=0;i<n;i++) cout<<"*** "<<node[i].a<<" "<<node[i].b<<" "<<node[i].flag<<endl;

	sort(node,node+n,cmp);
	long long ans=0;
	for (i=0;i<L;i++) {
		if (node[i].b==0) break;
		if (node[i].flag) ans+=node[i].a-node[i].b*2;
		ans+=node[i].b;
	}
	for (;i<n;i++)
		ans+=node[i].a;
	cout<<ans<<endl;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>L>>t>>n>>C;
		for (int i=0;i<C;i++) {
			scanf("%lld",&node[i].a);
			node[i].a*=2;
		}
		for (int i=C;i<n;i++)
			node[i].a=node[i-C].a;
		printf("Case #%d: ",++kase);
		solve();
	}
	return 0;
}
