#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000

int main(int argc, char **argv) {
	int caseNum = -1, caseN = 1;
//	freopen("test.txt", "r", stdin);

		freopen("B.out", "w", stdout);

//		freopen("B-small-attempt0.in","r",stdin);
//		freopen("B-small-attempt2.in","r",stdin);
		freopen("B-large.in","r",stdin);
	//	FILE *fp = fopen("test.txt", "r");
	//	FILE *fp = fopen("B-small-attempt0.in", "r");
//		FILE *fp = fopen("B-small-attempt1.in", "r");
//		FILE *fp = fopen("B-large.in", "r");
	//	FILE *fpw = fopen("B.out", "w");
	cin >> caseNum;

	while (caseNum--) {
		int C;
		unsigned long long L, P;
		cin >> L >> P >> C;

		long long t = C * C;

		long long  i = 0;
		if (L * C < P) {
			long long lt = t;
			while (lt * L < P) {
				lt *= t;
				i++;
			}
//			if ((lt / t * L) * C < P)
//				i--;
			i++;
//			if(i%2) i--;
		}

		long long res=0;
		while(i){
//			cout<<i;
			res++;
			if(i==1) break;
//			if(i%2) res++;
			i=(i-1)/2+1;

		}

		// fprintf(fpw, "Case #%d: %d\n", caseN,);
		//pay attention to endl!!!
		cout<<"Case #"<<caseN<<": "<< res<<endl;

		caseN++;
	}
}

