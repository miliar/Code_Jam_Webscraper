#include <iostream>
#include <vector>
using namespace std;
void solve(int test){
    long long l, p, c;
    cin >> l >> p >> c;
    if ( l * c >= p ) {cout << "Case #" << test << ": 0\n";return;}
    if ( l * c * c >= p ) {cout << "Case #" << test << ": 1\n";return;}
    int br1 = 0, br = 0,  br2 = 0;
    long long l1 = l, p1 = p;
    vector <long long> v;
    while ( l < p ){
        l *= c;
        if ( l < p )v.push_back(c);
        ++ br;
    }
    int mid = v.size() / 2;
    mid += 1;
    int x1 = mid / 2 + mid % 2;
    int broi = v.size() - mid - 1;
    int x2 = broi/ 2 + broi % 2;
    cout << "Case #" <<test << ": " <<  max(x1, x2) + 1 << endl;
}
int main(){
    int t;
    cin >> t;
    for ( int i = 0; i < t; ++i )
        solve(i + 1);
}
