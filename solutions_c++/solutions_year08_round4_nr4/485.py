#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define PB push_back
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define MP make_pair
#define PRESENT(container, element) (container.find(element) != container.end())
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define INF 1000000000
#define EPS 1e-10
#define CLEAR(c,n) memset((c), (n), sizeof(c))

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
#define FI first
#define SE second
typedef long long LL;
typedef istringstream ISS;
typedef ostringstream OSS;

int tc, k, l, p[16];
char s[1024], t[1024];
int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &tc);
	REP(itc, tc) {
		scanf("%d", &k);
		scanf("%s", s); l=strlen(s);
		s[l]=t[l]=0;
		int best=l;
		REP(i,k) p[i]=i;
		do {
			for (int i=0; i<l; i+=k) for (int j=0; j<k; ++j) t[i+j]=s[i+p[j]];
			int cnt=0;
			REP(i,l) if (t[i+1]!=t[i]) ++cnt;
			best<?=cnt;
		} while (next_permutation(p,p+k));
		printf("Case #%d: %d\n", itc+1, best);
	}
	return 0;
}

