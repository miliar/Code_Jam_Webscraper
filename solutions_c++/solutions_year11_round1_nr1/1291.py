#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

#define rep(i, n) for((i)=0; (i)<(int)(n); ++(i))

int GCD(int a, int b) {
    if(b==0) return a;
    else return GCD(b, a%b);
}

bool solve() {

    int n, d, g;
    cin >> n >> d >> g;

    if(g==0 && d!=0) return false;
    else if(g==100 && d!=100) return false;

    d = 100/GCD(d, 100);

    if(n>=d) return true;
    else return false;
}

int main() {

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int cases, cid;

    cin >> cases;

    rep(cid, cases) {
        if(solve()) cout << "Case #" << cid+1 << ": Possible" << endl;
        else cout << "Case #" << cid+1 << ": Broken" << endl;
    }

    return 0;
}
