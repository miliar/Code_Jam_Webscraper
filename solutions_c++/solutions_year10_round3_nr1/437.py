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
        int N;
        cin >> N;
        
        vector<int> arr;
        vector<int> arr2;
        REP(i, N) {
            int a,b;
            cin >> a >> b;
            arr.push_back(a);
            arr2.push_back(b);
        }
        int sum = 0;
        REP(i, N-1) {
            FOR(j, i+1, N-1) {
                int a1 = arr[i];
                int b1 = arr2[i];
                int a2 = arr[j];
                int b2 = arr2[j];
                if (((a1<a2) && (b1<b2)) ||
                    ((a1>a2) && (b1>b2))) {
                } else {
                    ++sum;
                }
            }
        }
		printf("Case #%d: %d\n", test, sum);
	}

	exit(0);
}
