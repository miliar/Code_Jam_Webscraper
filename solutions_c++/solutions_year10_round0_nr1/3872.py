#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <complex>
#include <bitset>
#include <numeric>
#include <valarray>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int inf = 987654321;

bool solve(int n, int k) {
    return (k & ((1 << n) - 1)) == ((1 << n) - 1);
}

int main() {
    int T;
    cin >> T;
    rep(I,T) {
        int n, k;
        cin >> n >> k;
        cout << "Case #" << I+1 << ": " << (solve(n,k) ? "ON" : "OFF") << endl;
    }
    return 0;
}
