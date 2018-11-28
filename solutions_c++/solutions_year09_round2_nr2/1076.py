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
#define debug if(0)printf

char cad[40];

int main() {
	int ncaso;
	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		scanf(" %s", &cad);
		vector<int> v;
		for (int i=0; i<22-strlen(cad); i++) v.PB(0);
		for (int i=0; i<strlen(cad); i++) v.PB((int)(cad[i]-'0'));

		next_permutation(v.begin(), v.end());
		int i=0;
		while (v[i]==0 && i<v.size()-1) i++;
		for (; i<v.size(); i++) printf("%d", v[i]);
		printf("\n");

	}

	return 0;
}
