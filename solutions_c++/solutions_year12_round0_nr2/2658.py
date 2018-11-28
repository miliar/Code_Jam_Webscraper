#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int a = 1; a <= T; ++a) {
        int N, S, p, t[40];
        cin >> N >> S >> p;
        for (int n = 0; n < N; ++n) {
            cin >> t[n];
        }
        int best = 0;
        for (int n = 0; n < N; ++n) {
            int k = t[n] / 3;
            switch(t[n] % 3) {
                case 0:
                    if (k >= p) {
                        best += 1;
                    }
                    else if (k+1 >= p && S > 0 && k != 0) {
                        best += 1;
                        --S;
                    }
                    break;
                case 1:
                    if (k+1 >= p) {
                        best += 1;
                    }
                    break;
                case 2:
                    if (k+1 >= p) {
                        best += 1;
                    }
                    else if (k+2 >= p && S > 0) {
                        best += 1;
                        --S;
                    }
                    break;
            }
        }
        cout << "Case #" << a << ": " << best << endl;
    }
}