#include <iostream>

using namespace std;

int k;
int rot(int n) {
    int t = n/k;
    n %= k;
    n *= 10;
    n += t;
    return n;
}

int main() {
    int T;
    cin >> T;
    for(int te = 1; te <= T; te++) {
        int A, B;
        cin >> A >> B;
        k = 1;
        while(k*10 <= A) k *= 10;
        int res = 0;
        for(int i = A; i <= B; i++) {
            int n = i;
            int m = rot(n);
            while(m != n) {
                if(m >= A && m <= B && m > n) res++;
                m = rot(m);
            }
        }
        cout << "Case #" << te << ": " << res << endl;
    }
    return 0;
}
