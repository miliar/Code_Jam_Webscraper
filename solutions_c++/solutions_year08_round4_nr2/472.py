// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> PDD;
typedef pair<ll,ll> PLL;

#define FOR(i,n)      for(int i=0;i<n;i++)
#define FORTO(i,a,b)  for(int i=a;i<=b;i++)
#define FORD(i,n)     for(int i=n-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=b;i>=a;i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define $ size()
#define ALL(x) (x).begin(),(x).end()
#define PB push_back


int main() {
	int C;
	scanf("%d", &C);
	FORTO(c,1,C) {
		int N, M, A;
		scanf("%d %d %d", &N, &M, &A);
		printf("Case #%d: ", c);
		FORTO(x1,0,N) FORTO(y1,0,M) FORTO(x2,0,N) FORTO(y2,0,M)
			if (x1*y2-x2*y1 == A) {
				printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
				goto next;
			}
		printf("IMPOSSIBLE\n");
		next:;
	}
	return 0;
}
