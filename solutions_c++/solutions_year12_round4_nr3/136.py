#include <iostream>
#include <cstring>
using namespace std;

#define MAXN 2048

typedef long long tint;

int N;
tint h[MAXN];

int findpeak(int cur) {
    int BEST = cur+1;
    for (int i=cur+2; i<N; i++) {
        if ((h[i]-h[cur])*((tint)(BEST-cur)) > (h[BEST]-h[cur])*((tint)(i-cur))) BEST = i;
    }
    return BEST;
}

int main() {
    int i, n[MAXN], peak, t, T;
    bool FLAG;

    cin >> T;
    for (t=1; t<=T; t++) {
        cin >> N;
        for (i=0; i<N-1; i++) {cin >> n[i]; n[i]--; h[i] = 0ULL;}
        h[N-1] = 0ULL;

        do {
//            for (i=0; i<N; i++) cout << h[i] << ' '; cout << endl;
            FLAG = true;
            for (i=0; i<N-1; i++) {
                peak = findpeak(i);
                if (peak != n[i]) {
//                    cout << "el pico de " << i+1 << " es " << peak+1 << " y deberia ser " << n[i]+1 << endl;
                    FLAG = false;
                    h[n[i]] = h[i] + ((tint)((n[i]-i)*(h[peak]-h[i])/((double)(peak-i))))+1ULL;
                    if (peak < n[i]) h[n[i]]++;
//                    cout << "subo el " << n[i]+1 << " a " << h[n[i]] << endl;
                    if (h[n[i]] > 1000000000ULL) break;
                }
            }
            if (i<N-1) break;
        } while (!FLAG);
        cout << "Case #"  << t << ":";
        if (FLAG) {for (i=0; i<N; i++) cout << ' ' << h[i]; cout << endl;}
        else cout << " Impossible" << endl;
    }

    return 0;
}
