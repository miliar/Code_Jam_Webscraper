/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
#include <climits>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define PRINTF(args...) printf(args)
// #define PRINTF(args...)

vector< pair<int, int> > A, B;

int test_nr = 0;

bool testuj(int ile_a, int ile_b) {
	int latacz1 = 0, latacz2 = 0;
	priority_queue<int> nowe_A, nowe_B;
	while(nowe_A.size()) nowe_A.pop();
	while(nowe_B.size()) nowe_B.pop();
	while(latacz1 != A.size() && latacz2 != B.size()) {
		while(!nowe_A.empty() && -nowe_A.top() <= A[latacz1].first) { nowe_A.pop(); ++ile_a; }
		while(!nowe_B.empty() && -nowe_B.top() <= B[latacz2].first) { nowe_B.pop(); ++ile_b; }
		
		if(A[latacz1].first <= B[latacz2].first) {
			nowe_B.push(-A[latacz1].second);
			++latacz1;
			--ile_a;
			if(ile_a < 0) return false;
		} else {
			nowe_A.push(-B[latacz2].second);
			++latacz2;
			--ile_b;
			if(ile_b < 0) return false;
		}
	
	}
	
	while(latacz1 != A.size()) {
		while(!nowe_A.empty() && -nowe_A.top() <= A[latacz1].first) { nowe_A.pop(); ++ile_a; }
		++latacz1;
		--ile_a;
		if(ile_a < 0) return false;
	}
	
	while(latacz2 != B.size()) {
		while(!nowe_B.empty() && -nowe_B.top() <= B[latacz2].first) { nowe_B.pop(); ++ile_b; }
		++latacz2;
		--ile_b;
		if(ile_b < 0) return false;
	}
	return true;
}

void testcase() {
	int na, nb, tt;
	scanf("%d", &tt);
	scanf("%d%d", &na, &nb);
	A.clear();
	B.clear();
	REP(i,na) {
		char buf1[10], buf2[10];
		scanf("%s%s", buf1, buf2);
		int pocz = 0, kon = 0;
		pocz = ((buf1[0]-'0')*10 + (buf1[1]-'0'))*60 + ((buf1[3]-'0')*10 + (buf1[4]-'0'));
		kon = ((buf2[0]-'0')*10 + (buf2[1]-'0'))*60 + ((buf2[3]-'0')*10 + (buf2[4]-'0'));
		A.push_back( make_pair(pocz, kon+tt) );
	}
	
	REP(i,nb) {
		char buf1[10], buf2[10];
		scanf("%s%s", buf1, buf2);
		int pocz = 0, kon = 0;
		pocz = ((buf1[0]-'0')*10 + (buf1[1]-'0'))*60 + ((buf1[3]-'0')*10 + (buf1[4]-'0'));
		kon = ((buf2[0]-'0')*10 + (buf2[1]-'0'))*60 + ((buf2[3]-'0')*10 + (buf2[4]-'0'));
		B.push_back( make_pair(pocz, kon+tt) );
	}
	
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	
	int res_a = 10000, res_b = 10000;
	REP(ile_a, na+1) REP(ile_b, nb+1)
		if(ile_a+ile_b < res_a + res_b && testuj(ile_a, ile_b)) {
			res_a = ile_a;
			res_b = ile_b;
		}
	
	printf("Case #%d: %d %d\n", ++test_nr, res_a, res_b);
}

int main() {
	int t;
	for(scanf("%d", &t);t--;) testcase();
	return 0;
}
