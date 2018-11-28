#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>

using namespace std;

const int MAXN = 1005;

int _t;
int n, A[MAXN], B[MAXN], res;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    scanf("%d", &_t);
    for (int cas = 1; cas <= _t; cas++) {
        scanf("%d", &n);
        res = 0;
        for (int i = 0; i < n; i++) scanf("%d%d", &A[i], &B[i]);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if ((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j])) res++;
            }
        }
        printf("Case #%d: %d\n", cas, res / 2);
    }
	return 0;
}

