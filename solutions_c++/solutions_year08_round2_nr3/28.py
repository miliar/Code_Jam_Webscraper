#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// BEGIN CUT HERE
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
// END CUT HERE

class RangeTree {
    private:
        int size;
        VI sum;
    public:
        RangeTree(int N)
        {
            for (size = 1; size < N; size *= 2) ;
            sum.resize(2*size);
        }
        
        void increase(int pos, int value)
        {
            int L = 0, R = size, ind = 0;
            while (L < R) {
                sum[ind] += value;
                if (L == R-1)
                    return;
                int M = (L+R) >> 1;
                ind *= 2;
                if (pos < M) {
                    R = M;
                    ind += 1;
                } else {
                    L = M;
                    ind += 2;
                }
            }
        }

        /* Get sum from [0; R) */
        int total(int N)
        {
			if (N == 0)
				return 0;
            int L = 0, R = size, ind = 0, total = 0;
            while (N > L) {
                if (R == N)
                    return total + sum[ind];
                int M = (L+R) >> 1;
                if (N >= M) {
                    total += sum[ind*2+1];
                    L = M;
                    ind = ind*2+2;
                } else {
                    R = M;
                    ind = ind*2+1;
                }
            }
            return total;
        }

		int total(int L, int R) {
			return total(R) - total(L);
		}
};
 

void solve(int iTest)
{
	int K, N;
	scanf("%d %d", &K, &N);
	VI d(N);
	REP(i, N)
		scanf("%d", &d[i]);

	VI deck(K, -1);
	RangeTree rt(K);
	REP(i, K)
		rt.increase(i, +1);

	int index = 0;
	REP(i, K) {
		int query = (i + 1) % (K - i);
		if (query == 0)
			query = K - i;

		int right = rt.total(index, K);
		int L, R;
		if (query <= right) {
			L = index;
			R = K;
		} else {
			L = 0;
			R = index;
			query -= right;
		}

		while (R-L > 1) {
			int M = (L+R) >> 1;
			int q = rt.total(L, M);
			if (query <= q) {
				R = M;
			} else {
				L = M;
				query -= q;
			}
		}
		index = L;

		deck[ index ] = i;
		rt.increase(index, -1);
	}

	
	cout << "Case #" << iTest << ":";
	REP(i, N)
		cout << " " << deck[d[i]-1] + 1;
	cout << endl;
}

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		solve(iTest);
	return 0;
}
