/*
 ID: sunhaowen
 PROG: acm/icpc
 LANG: C++
 */
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

#define max_int       INT_MAX / 2
#define max_long      0xFFFFFFFFFFFFFFFLL / 2
#define two(a)        (1 << (a))
#define eps           1e-6
#define FF(i, a, b)   for (int i = (a); i <= (b); i++)
#define FFD(i, a, b)  for (int i = (a); i >= (b); i--)

int T, n, c[1005];
int main(int argc, char** argv) {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cin >> n;
        int ans = 0;
        int sum = 0, small = max_int;
        for (int i = 1; i <= n; i++) {
            cin >> c[i];
            ans ^= c[i];
            sum += c[i];
            small = min(small, c[i]);
        }
        if (ans == 0) {
            cout << "Case #" << ca << ": " << sum - small << endl;
        } else {
            cout << "Case #" << ca << ": " << "NO" << endl;
        }
    }

    return (EXIT_SUCCESS);
}

