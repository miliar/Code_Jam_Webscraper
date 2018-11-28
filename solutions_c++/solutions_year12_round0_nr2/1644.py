#include <iostream>
using namespace std;

int main() {
    int N, S, P, n, tmp, RES, i, t, T;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N;
        cin >> S;
        cin >> P;
    
        RES = 0;
        for (i=0; i<N; i++) {
            cin >> tmp;
            n = tmp/3;
            if (tmp%3 != 0) n++;
            if (n >= P) RES++;
            else if (n == P-1 && S > 0 && n > 0 && tmp%3 != 1) {RES++; S--;}
        }
        cout << "Case #" << t << ": " << RES << endl;
    }

    return 0;
}
