#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int pow(int a, int b) {
    if (b == 0) return 1;
    int aux = pow(a,b/2);
    aux *= aux;
    if (b%2 == 1) aux *= a;
    return a;
}

int main() {
    int t; cin >> t;
    int c = 1;
    int n = 30;
    vector<int> v(31);
    v[0] = 1;
    for (int i = 1; i < n; ++i) v[i] = 1 + 2*v[i - 1]; 
    while (t--) {
        int n1, k; cin >> n1 >> k;
        while(k > v[n1 - 1]) k -= v[n1 - 1] + 1;
        if (v[n1 - 1] == k) cout <<"Case #" << c++ << ": ON" << endl;
        else cout <<"Case #"<< c++ << ": OFF" << endl;
    }
}
 
