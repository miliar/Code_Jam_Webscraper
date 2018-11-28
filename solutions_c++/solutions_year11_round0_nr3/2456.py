#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cstring>

#define pii pair <int, int>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back

const int INF = 2147483647;
const double EPS = 1E-9;
const double PI = acos(-1);

using namespace std;

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, n, a, S, M, X;
    cin >> t;
    for(int q=1; q<=t; ++q) {
        cin >> n;
        S = 0; M = INF; X = 0;
        for(int i=0; i<n; ++i) {
            cin >> a;
            S += a;
            M = min(M, a);
            X = X^a;
        }
        if(X != 0)
            cout << "Case #" << q << ": NO" << endl;
        else
            cout << "Case #" << q << ": " << S-M << endl;
    }

    return 0;
}
