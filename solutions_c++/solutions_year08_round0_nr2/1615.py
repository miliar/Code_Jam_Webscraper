#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)

using namespace std;

char c[110];

struct ev { 
	int t, p, q;
	ev(int a, int b, int c) : t(a), p(b), q(c) {}
};

struct cmp {
	bool operator()(const ev &a, const ev &b) const {
		if(a.t==b.t)
			return  a.p<b.p;
		return a.t>b.t;
	}
};

inline int get_1() {
	return ((10*(c[0]-'0')+c[1]-'0')*60)+((c[3]-'0')*10+c[4]-'0');
}

inline int get_2() {
	return ((10*(c[6]-'0')+c[7]-'0')*60)+((c[9]-'0')*10+c[10]-'0');
}

int main(void) {
	int t, x, n, m, i, j, k, resa, resb, T;
	scanf("%d", &t);
	REP(x,t) {
		scanf("%d%d%d", &T, &n, &m); gets(c);
		priority_queue<ev, vector<ev>, cmp> S;
		queue<int> A, B; resa=0; resb=0;
		REP(i,n) {
			gets(c);
			S.push(ev(get_1(),0,0));
			S.push(ev(get_2(),1,0));
		}
		REP(i,m) {
			gets(c);
			S.push(ev(get_1(),0,1));
			S.push(ev(get_2(),1,1));
		}
		while(S.size()>0) {
			ev p=S.top(); S.pop();
			if(p.p==1) {
				if(p.q==0)
					B.push(p.t);
				else
					A.push(p.t);
			}
			else {
				if(p.q==0) {
					if(A.size()>0 && A.front()+T<=p.t)
						A.pop();
					else
						++resa;
				}
				else {
					if(B.size()>0 && B.front()+T<=p.t)
						B.pop();
					else
						++resb;
				}
			}
		}
		printf("Case #%d: %d %d\n", x+1, resa, resb);
	}
	return 0;
}
