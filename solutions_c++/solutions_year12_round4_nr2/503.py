#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
const int N = 1005;
int a[N], n, w, l, c[N];
double x[N], y[N];
void solve(){
    cin >> n >> w >> l;
    for (int i = 0; i < n; i++){
        cin >> a[i];
        a[i] *= 2;
        c[i] = i;
    }
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[j] > a[i]){
                swap(a[i], a[j]);
                swap(c[i], c[j]);
            }
    int rrr = 0;
   /* if (w < l)  {
        swap(w, l);
        rrr = 1;
    }*/
    int i = 0; int ww = w;
    while (ww >= 0){
        int ll = l, max = 0;
        while ( (ll == l || ll >= a[i] / 2) && i < n){
            if (ww == w){
                x[c[i]] = 0;
            } else {
                x[c[i]] = w - ww + a[i] / 2;
            }
            if (ll == l) { y[c[i]] = 0; ll -= a[i] / 2; }
             else {y[c[i]] = l - ll + a[i] / 2; ll -= a[i];}

            if (a[i] > max) max = a[i];
            i++;
        }
        if (i >= n) break;
        if (ww == w) ww -= max / 2;
        else ww -= max;
    }
    for (int i = 0; i < n; i++){
        //if (rrr == 1) swap(x[i], y[i]);
        printf(" %.0f %.0f", x[i], y[i]);
    }
    cout << endl;
}
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d:", i);
        solve();
    }
}
