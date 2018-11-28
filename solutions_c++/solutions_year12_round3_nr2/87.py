#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

typedef long double ld;

ld t[2000], x[2000];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cout.precision(20);
    int T;
    cin >> T;
    for (int CT = 1; CT <= T; CT++) {
        cout << "Case #" << CT << ":" << endl;
        ld D;
        cin >> D;
        int N, A;
        cin >> N >> A;
        for (int i = 0; i < N; i++)
            cin >> t[i] >> x[i];
        if ((N >= 1) && (x[0] >= D)) N = 0; else
            while (x[N-2] >= D) N--;
        if (x[N-1] > D) {
            t[N-1] = t[N-2] + (t[N-1] - t[N-2]) * (D - x[N-2]) / (x[N-1]-x[N-2]);
            x[N-1] = D;
        }
        for (int j = 0; j < A; j++) {
            ld s = 0, a;
            cin >> a;
            for (int i = 0; i < N; i++)
                s = max(s, t[i] - sqrt(2*x[i]/a));
            s += sqrt(2*D/a);
            cout << s << endl;
        }
    }
    return 0;
}
