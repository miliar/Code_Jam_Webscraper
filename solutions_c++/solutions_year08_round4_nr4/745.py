#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(1)printf
#define MAXINT 1000000000;

int perm[17];
char s[100000], s2[100000];
int k;

int contar(char *str) {
	int res=1;
	for (char *p=str+1; *p; p++) {
		if (*p!=*(p-1)) res++;
	}
	return res;
}

int main() {
	int ncaso;
	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		scanf(" %d %s", &k, s);
		REP(i, k) {perm[i]=i;}
		int minres=strlen(s);
		strcpy(s2, s);
		do {
			//REP(j, k) debug("%d,", perm[j]);debug("\n");
			for (int i=0; i<strlen(s); i+=k) {
				REP (j, k) {
					s2[i+j]=s[i+perm[j]];
				}
			}
			minres=min(minres, contar(s2));
		} while (next_permutation(perm, perm+k));
		printf("%d\n", minres);
	}

	return 0;
}
