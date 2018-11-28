#include <iostream>
using namespace std;
int n, k;
void solve(int test){
    cin >> n >> k;
    cout << "Case #" << test << ": ";
    if ( k % (1 << n) == (1 << n) - 1 ) cout << "ON\n";
    else cout << "OFF\n";
}
int main(){
    int tmp;
    cin >> tmp;
    for ( int i = 0; i < tmp; ++i )
        solve(i + 1);
}