#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

void solve(int T) {
    int n, k;
    cin >> n >> k;
    int a = k;
    int cn = 0;
    for(int i=0; i+1<n; i++) {
        cn += a%2;
        a /= 2;
    }
    cn += a%2;
    //cout << cn << " " << n << endl;
    cout << "Case #" << T << ": " << (((a%2)==1 && cn==n) ? "ON" : "OFF") << endl;
}

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=0; t<T; t++)
        solve(t+1);
    return 0;
}
