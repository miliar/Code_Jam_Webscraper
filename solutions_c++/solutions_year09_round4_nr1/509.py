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

using namespace std;

const int nMax = 42;

char S[nMax];
int tab[nMax];

void testcase(int testNr) {
	
	int N;
	scanf("%d",&N);
	FOR(i,0,N) {
		scanf("%s",S);
		int maxi = 0;
		FOR(j,0,N) if(S[j]=='1')
			maxi = j;
		tab[i] = maxi;
	}
	
	int res = 0;
	FOR(i,0,N) {
		int best = i;
		while(tab[best] > i)
			best++;
		while(best != i) {
			swap(tab[best], tab[best-1]);
			best--;
			res++;
		}
	}
	
	printf("Case #%d: %d\n", testNr, res);
}

int main() {
	int t;
	scanf("%d",&t);
	FOR(i,0,t)
		testcase(i+1);
}
