#include<cstdio>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<stack>
#include<map>
#include<queue>

#define FOR(i,a,b) for(int i=(int)(a); i<(int)(b); ++i)
#define FORE(it,C) for(__typeof(C.begin()) it=C.begin(); it!=C.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long double LD;

using namespace std;

struct Circle {
	int r;
	int x,y;
};

Circle tab[3];

LD go(Circle &A, Circle &B) {
	LD dist = sqrt((A.x-B.x)*(A.x-B.x) + (A.y-B.y)*(A.y-B.y));
	dist += A.r;
	dist += B.r;
	dist /= 2;
	return dist;
}

void testcase(int testNr) {

	int N;
	scanf("%d",&N);
	
	FOR(i,0,N)
		scanf("%d %d %d",&tab[i].x,&tab[i].y,&tab[i].r);
		
	LD res;
		
	if(N==1) {
		res = tab[0].r;
	} else if(N==2) {
		res = max(tab[0].r, tab[1].r);
	} else {			//N==3
		res = 1000000.0;
		res = min(res, max(go(tab[0],tab[1]), (LD)tab[2].r));
		res = min(res, max(go(tab[0],tab[2]), (LD)tab[1].r));
		res = min(res, max(go(tab[1],tab[2]), (LD)tab[0].r));
	}
	
	printf("Case #%d: %.7llf\n",testNr, res);
}

int main() {
	int t;
	scanf("%d",&t);
	FOR(i,0,t)
		testcase(i+1);
}
