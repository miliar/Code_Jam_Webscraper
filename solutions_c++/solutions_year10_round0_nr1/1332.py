#include <string>
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
#include <cstring>
#include <ctime>
#include <cassert>


using namespace std;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define ALL(M) (M).begin(), (M).end()
#define CLR(M, v) memset(M, v, sizeof(M))
#define SI(V) (int)(V.size())
#define PB push_back

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;

const int INF = 0x3F3F3F3F;
const double EPS = 1E-14;

template<class T> T SQR(T x) { return x*x; }

////////////////////////////////////////////////////////////////////////////////

int N, K;

int main() {
    
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);
    
    int TC;
    scanf("%d ", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        // Read input.
        scanf("%d %d", &N, &K);
        
        // Prints result.
        int M = (1<<N)-1;
        printf("Case #%d: %s\n", tc, ((M&K)==M) ? "ON" : "OFF");
    }

	return 0;
}
