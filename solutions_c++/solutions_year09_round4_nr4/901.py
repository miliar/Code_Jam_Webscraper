#include <iostream>
#include <cmath>
using namespace std;
struct plant{
    double x, y, r;
};
plant a[64];
int used[64][64], n;
void scan(){
    cin >> n;
    for ( int i = 0; i < n; ++i )
        cin >> a[i].x >> a[i].y >> a[i].r;
}
double dist(plant a, plant b){
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * ( a.y - b.y));
}
double max(double a, double b){
    if ( a > b ) return a;
    return b;
}
void solve(int q){
    cout << "Case #" << q << ": ";
    if ( n == 1 ){ cout << a[0].r << endl; return;}
    if ( n == 2 ) { cout << max (a[0].r, a[1].r) << endl;return;}
    for ( int i = 0; i < 64; ++i ) memset(used, 0, sizeof(used));
    double mn = 999999999, mn1;
    mn1 = mn;
    int i1, j1;
    for ( int i = 0; i < n; ++i )
        for ( int j = i + 1; j < n; ++j )
            if ( dist(a[i], a[j]) + a[i].r + a[j].r < mn ){ mn = dist(a[i], a[j]) + a[i].r + a[j].r; i1 = i; j1 = j; }
    used[i1][j1] = used[j1][i1] = 1;
    if ( i1 != 0 && j1 != 0 ) cout << max(mn, a[0].r)/2. << endl;
    if ( i1 != 1 && j1 != 1 ) cout << max(mn, a[1].r)/2. << endl;
    if ( i1 != 2 && j1 != 2 ) cout << max(mn, a[2].r)/2. << endl;
    
}
int main(){
    int t;
    cin >> t;
    for ( int i = 0; i < t; ++i ){
        scan();
        solve(i + 1);
    }
}
