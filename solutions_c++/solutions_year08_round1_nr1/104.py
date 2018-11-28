#include <iostream>
using namespace std;

const int mx = 1000;
long long a[mx], b[mx], sum;
int i, j, ts, o, n;

main() {
       freopen("b0.in", "r", stdin);
       freopen("b0.out", "w", stdout);
       
       for (cin>>ts; ++o<=ts; ) {
           cin >> n;
           for (i=0; i<n; i++) cin >> a[i];
           for (i=0; i<n; i++) cin >> b[i];
           sort(a, a+n);
           sort(b, b+n);
           for (i=sum=0; i<n; i++) sum += a[i]*b[n-i-1];
           cout << "Case #" << o << ": " << sum << endl;
       }
}
