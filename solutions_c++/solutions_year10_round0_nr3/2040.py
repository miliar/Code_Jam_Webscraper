#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

void start() {
    int n; cin>>n;
    FOR(_i,n) {
		int R,k,N; cin>>R>>k>>N;
		vi g(N); FOR(i,N) cin>>g[i];

		int64 sum=0;
		int day=1;

		map<int,int> occurs;
		vector<int64> value;
		occurs[0]=0;
		value.push_back(0);

		int qIdx = 0;
		while(true) {
			int leftSeats=k;
			int startQIdx = qIdx;
			while(leftSeats >= g[qIdx])
			{
				sum += g[qIdx];
				leftSeats -= g[qIdx];
				if (++qIdx == N) qIdx = 0;

				if (qIdx == startQIdx) break;
			}

			value.push_back(sum);
			if (occurs.count(qIdx) != 0) break;
			occurs[qIdx] = day;

			++day;
		}

		int64 res = 0;

		if (R >= day) {
			R -= occurs[qIdx];
			res += value[ occurs[qIdx] ];

			int len = day - occurs[qIdx];
			sum -= value[ occurs[qIdx] ];
			res += int64(R / len) * sum;
			R %= len;
		} else {
			qIdx = 0;
		}

		FOR(i, R) {
			int leftSeats=k;
			while(leftSeats >= g[qIdx])
			{
				res += g[qIdx];
				leftSeats -= g[qIdx];
				if (++qIdx == N) qIdx = 0;
			}
		}

        printf("Case #%d: %lld\n", _i+1, res);
    }
}

int main(void) {
#ifdef LOCAL
	extern void runtest();
	runtest();
#else
	start();
#endif

	return 0;
}
