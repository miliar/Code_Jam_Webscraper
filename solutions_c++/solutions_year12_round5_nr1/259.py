#include <stdio.h>
#include <string.h>
#include <algorithm>

int n;
struct node {
	int p, l, id;
	
	node(){}
	node(int _p, int _l, int _id) {
		p = _p;
		l = _l;
		id = _id;
	}
	
	void get(int _id) {
		scanf("%d%d",&p, &l);
		id = _id;
	}
	
	bool operator < (const node &t) const {
		return (p > t.p || (p == t.p && (l > t.l || (l == t.l && id < t.id))));
	}
} S[1010];

int main() {

	int t, cases=0;
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			S[i].id = i;
			scanf("%d", &S[i].l);
		}
		for(int i=0;i<n;++i)
			scanf("%d", &S[i].p);
			
			
		std::sort(S, S+n);
		printf("Case #%d:", ++cases);
		for(int i=0;i<n;++i)
			printf(" %d", S[i].id);
		puts("");
	}

	return 0;
}
