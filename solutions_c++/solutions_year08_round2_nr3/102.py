#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

struct El {
	int ind;
	El *next, *prev;
	El(int _ind): ind(_ind) { next=prev=0; }
};

const int kMax = 5005;

int res[kMax];

void testcase(int tNum) {
	
	int K;
	scanf("%d",&K);
	
	El *beg = new El(0);
	El *p = beg;
	FOR(i,1,K) {
		p->next = new El(i);
		p->next->prev = p;
		p = p->next;
	}
	p->next = beg;
	beg->prev = p;
	
	FOR(i,0,K) res[i] = K;
	
	p = beg;
	FOR(i,1,K) {
		FOR(j,1,i) p = p->next;
		p->prev->next = p->next;
		p->next->prev = p->prev;
		res[p->ind] = i;
		El *q = p->next;
		delete p;
		p = q;
	}
	res[p->ind] = K;
	
	int n;
	scanf("%d",&n);
	printf("Case #%d: ",tNum);
	while(n--) {
		int a;
		scanf("%d",&a);
		printf("%d ",res[a-1]);
	}
	printf("\n");
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
