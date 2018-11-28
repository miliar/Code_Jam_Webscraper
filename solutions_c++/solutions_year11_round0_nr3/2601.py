#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

#define mp make_pair

using namespace std;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int nt, n, t;
    cin>>nt;
    int i, j, x, m, s;
    int a;
    for(t=1; t<=nt; ++t) {
        cin>>n;
        x = 0;
        s = 0;
        m = 1<<25;
        for(i=0; i<n; ++i) {
            cin>>a;
            x ^= a;
            m = min(m, a);
            s += a;
        }
        cout<<"Case #"<<t<<": ";
        if (n < 2 || x != 0) {
            cout<<"NO";
        } else {
            cout<<s-m;
        }
        cout<<endl;
    }
    return 0;
}
