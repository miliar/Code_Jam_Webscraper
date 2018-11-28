#include <iostream>
#include <algorithm>
#include <vector>

#define FR(i, n) for (int i=0; i<(n); i++)
#define FOR(i, a, b) for (int i=(a); i<=(b); i++)

using namespace std;

int ntest, res, sxor, sum;
int n;
int a[1111];

void process() {
     cin >> n;
     FR(i, n) cin >> a[i];
     
     sum = 0;
     sxor = 0;
     FR(i, n) sxor ^= a[i], sum += a[i];
     
     res = -1;
     if (sxor==0) {
        int amin = a[0];
        FR(i, n) amin <?= a[i];
        res = sum - amin;
     }
}

int main() {
    
    freopen("C-large.in", "rt", stdin);
    freopen("c2.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        printf("Case #%ld: ", i);
        process();   
        if (res<0) cout << "NO\n";
        else cout << res << endl;     
    }    
    
    return 0;
}
