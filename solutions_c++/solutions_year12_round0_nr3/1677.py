#include <iostream>
#include <set>
using namespace std;

int main() {
    int A, B, MOD, n, m, RES, T, t;
    set<int> tmp;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> A;
        cin >> B;
    
        MOD = 1;
        while (10*MOD <= A) MOD *= 10;
    
        RES = 0;
        for (n=A; n<=B; n++) {
            m = n; tmp.clear();
            do {
                m = (m%10)*MOD + m/10;
                if (m >= A && m <= B) tmp.insert(m);
            } while (m!=n);
            RES += tmp.size()-1;
        }
        cout << "Case #" << t << ": " << RES/2 << endl;
    }

    return 0;
}
