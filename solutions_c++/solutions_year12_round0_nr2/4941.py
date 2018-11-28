#include <iostream>

using namespace std;

int main()
{
    int T, N, S, p, t;
    int test, i, j, k;
    int total;
    int Sin;
    cin >> T;
    for (test = 1; test <= T; test++) {
        cin >> N >> S >> p;
        Sin = 0;
        total = 0;
        for (i = 0; i < N; i++) {
            cin >> t;
            if (t == 0) {
                if (p == 0)
                    total++;
            }
            else if (t%3 == 0){
                if (t/3 >= p)
                    total++;
                else if (t/3 == p-1) {
                    Sin++;
                }

            }
            else if ((t+1)%3 == 0) {
                if (((t+1)/3)>= p)
                    total++;
                else if ((t+1)/3 == p-1) {
                    Sin++;
                }
            }
            else if ((t-1)%3 == 0) {
                    if (((t-1)/3 + 1 )>= p)
                        total++;
            }
        }
        if (Sin > S)
            total += S;
        else
            total += Sin;
        cout << "Case #" << test << ": " << total << endl;

    }

    return 0;
}
