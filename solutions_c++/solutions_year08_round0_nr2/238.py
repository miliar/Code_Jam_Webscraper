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

struct Trip {
	int s,e;
	int type;
	bool vis;
	Trip(int _s=0, int _e=0, int _type=0): s(_s), e(_e), type(_type), vis(false) { }
};

const int nMax = 205;

Trip tab[nMax];

void testcase(int tNum) {

	int res[2];
	res[0] = res[1] = 0;
	
	int nA, nB, n, turn;
	scanf("%d %d %d",&turn,&nA,&nB);
	n = nA+nB;
	
	FOR(i,0,nA) {
		int hs,ms,he,me;
		scanf("%d:%d %d:%d",&hs,&ms,&he,&me);
		tab[i] = Trip(hs*60+ms, he*60+me, 0);
	}
	FOR(i,0,nB) {
		int hs,ms,he,me;
		scanf("%d:%d %d:%d",&hs,&ms,&he,&me);
		tab[nA+i] = Trip(hs*60+ms, he*60+me, 1);
	}
	
	FOR(i,1,n) FORD(j,i+1,1) if(tab[j].s<tab[j-1].s)
		swap(tab[j], tab[j-1]); else
		break;
		
	int num = 0;
	while(num<n) {
		int cur = 0, next, ti=0;
		while(tab[cur].vis) cur++;
		
		res[tab[cur].type]++;
		next=tab[cur].type;
		
		while(cur<n) if(tab[cur].type==next && !tab[cur].vis && tab[cur].s>=ti) {
			num++;
			tab[cur].vis = true;
			next = 1-next;
			ti = tab[cur].e+turn;
		} else cur++;
		
	}	
	
	printf("Case #%d: %d %d\n",tNum,res[0],res[1]);
	
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
