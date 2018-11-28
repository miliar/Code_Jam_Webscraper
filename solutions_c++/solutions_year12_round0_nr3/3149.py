
#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

void solve(long a, long b);

int main(void) {
    long t, a, b;
    long i;

    cin >> t;
    
    for (i = 0; i < t; i++) {
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": ";
        solve(a, b);
        cout << endl;
    }
    
    return 0;
}

void solve(long a, long b) {
    long num, max_dec, aux, dec = 1;
    long i, j;
    list<long> v;
    
    i = a;
    
    while (i > 0) {
        i /= 10;
        dec *= 10;
    }
    
    dec /= 10;
    
    for (i = a; i <= b; i++) {
        aux = dec;
        max_dec = dec;

        for (j = 10; j <= aux; j *= 10) {
            num = max_dec * (i % j) + i/j;
            if (num >= i && num <= b && num != i) v.push_back(num);
            max_dec /= 10;
        }
    }
    
    v.unique();
    cout << v.size();
}
