//============================================================================
// Name        : B.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
    long tnum, k, n, t;
    long b;
    cin >> tnum;
    for (long ti = 1; ti <= tnum; ti++) {
        long cnt = 0;
        long x[50], v[50];
        bool c[50] = { 0 };
        cin >> n >> k >> b >> t;
        for (long i = 0; i < n; i++)
            cin >> x[i];
        for (long i = 0; i < n; i++)
            cin >> v[i];
        long need = k;
        for (long i = 0; i < n; i++) {
            c[i] = (b <= x[i]+v[i]*t);
            if (c[i])
                need--;
        }
        if (need > 0)   {
            cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
            continue;
        }
        for (long i = n - 1; i >= 0; i--) {
            if (c[i])    {
                if (k-- == 0)
                    break;
                for (long j = i + 1; j < n; j++) {
                    if (!c[j])
                        cnt++;
                };
            }
        }
        cout << "Case #" << ti << ": " << cnt << endl;
    }
    return 0;
}
