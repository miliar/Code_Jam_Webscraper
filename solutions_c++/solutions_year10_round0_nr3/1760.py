#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	FOR(test, 1, T) {
        long R,k,N;
        cin >> R >> k >> N;
        vector<long> gains(N);
        vector<int> skips(N);
        vector<long> Q;
        REP(i, N) {
            long t;
            cin >> t;
            Q.push_back(t);
        }
        REP(i, N) {
            long gain = 0;
            int skip = 0;
            REP(j, N) {
                long t = gain + Q[(i+j)%N];
                if (t > k) {
                    break;
                }
                gain = t;
                skip++;
            }
            skips[i] = skip;
            gains[i] = gain;
        }
        int cur = 0;
        vector<bool> seen(N);
        REP(i, N) {
            cur += skips[cur];
            if (cur >= N) cur -= N;
            if (seen[cur]) break;
        }
        int repeat_s = cur;
        long gain_oneround = 0;
        int n_oneround = 0;
        REP(i, N) {
            gain_oneround += gains[cur];
            cur += skips[cur];
            if (cur >= N) cur -= N;
            n_oneround ++;
            if (cur == repeat_s) break;
        }
    
        long gain = 0;
        cur = 0;
        REP(i, R) {
            if (cur == repeat_s) {
                int njump = (R-1-i) / n_oneround;
                gain += njump * gain_oneround;
                i += njump * n_oneround;
            } 
            gain += gains[cur];
            cur += skips[cur];
            if (cur >= N) cur -= N;
        }
		printf("Case #%d: %ld\n", test, gain);
	}

	exit(0);
}
