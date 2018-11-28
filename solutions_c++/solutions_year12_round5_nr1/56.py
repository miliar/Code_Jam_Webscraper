#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

struct grr {
	long long p,q;
	grr(long long p, long long q) {this->p = p; this->q = q;}
};
bool operator<(grr a, grr b) {
	return a.p * b.q < b.p * a.q;
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);

		vector<pair<grr,int> > v;
		int n; scanf("%d",&n);
		vector<int> l;
		for (int i = 0; i < n; i++) {
			int ll; scanf("%d",&ll);
			l.push_back(ll);
		}
		for (int i = 0; i < n; i++) {
			int p; scanf("%d",&p);
			v.push_back(make_pair(grr(-p,l[i]),i));
		}
		sort(v.begin(),v.end());
		printf("Case #%d:",test);
		for (int i = 0; i < n; i++) {
			printf(" %d",v[i].second);
		}
		printf("\n");
		
		
	}
}
