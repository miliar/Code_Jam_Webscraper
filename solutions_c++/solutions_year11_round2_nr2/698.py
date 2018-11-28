#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

int ntest, P[205], V[205], D, C;
long long sum;

bool check (long long x) {
    double t = x / 2.0, left = -10000000000000000ll, right = -10000000000000000ll;
    for (int i = 0; i < C; i++) {
        left = max(P[i] - t, right + D);
        right = min(P[i] + t, left + (V[i] - 1) * D) ;
        if (right - left < (V[i] - 1) * D) return false;
    }
    return true;
}

void process(){
    long long l, r, m, lm;
    l = 0, r = sum * D * 2;
    do {
        long long m = (l + r) / 2;
        if (check(m)) {
            lm = m;   
            r = m - 1;
        } else l = m + 1;
    } while (l <= r);
    cout << lm / 2.0 << endl;
};

int main () {
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    cin >> ntest;
    for (int k = 1; k <= ntest; k++) {
        cin >> C >> D;
        cout << "Case #" << k << ": ";
        for (int i = 0; i < C; i++) {
            cin >> P[i] >> V[i];   
            sum += V[i];
        }   
        process();
    }
//    getch();
    return 0;   
}
