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

const int MAXV = 1010;

i64 PROFIT[MAXV];
int NEXT[MAXV], PAI[MAXV];
int PC, L; i64 C;

int R, K, N;
int G[MAXV];

int main() {
    
//	freopen("C.in","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.ans","w",stdout);

    int p, q;
    i64 s;

    int TC;
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        // Read input.
        scanf("%d%d%d", &R, &K, &N);
        FOR(i,0,N) scanf("%d", &G[i]);
        
        // Initialize.
        CLR(PAI,-1); CLR(NEXT,-1); CLR(PROFIT,0);
        
        // Pre-compute cycle and next values.
        q = 0;
        while (NEXT[q]==-1) {
            s = 0; p = q;
            do { s += G[q]; q = (q+1)%N; } while (s+G[q] <= K && q != p);
            PROFIT[p] = s; NEXT[p] = q; PAI[q] = p;
        }
        PC = q; C = 0; L = 0;
        do { q = PAI[q]; C += PROFIT[q]; L++; } while (q != PC);
        
        // Compute total profit.
        i64 ret = 0;
        for (p = 0; p != PC && R; R--, p = NEXT[p]) ret += PROFIT[p];
        ret += C*(R/L); R -= L*(R/L);
        for (p = PC; R; R--, p = NEXT[p]) ret += PROFIT[p];
        
        // Prints result.
        printf("Case #%d: %lld\n", tc, ret);
    }

	return 0;
}
