/* Google Code Jam Qualifying Round - Dancing With the Googlers */

#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
        int T; cin >> T;
        for (int cT = 1; cT <= T; cT++) {
                int N, S, p; cin >> N >> S >> p;
                int count = 0, surprising_count = 0;
                for (int i = 0; i < N; i++) {
                        int t, q; cin >> t;
                        
                        /* edge case when we cannot take away any */
                        if (t < 3) {
                                q = t == 0 ? 0 : 1;
                                if (q >= p) count++;
                                goto cont;
                        }

                        /* determine if p reached by nonsurprising score */
                        q = t / 3;
                        if (t % 3 != 0) q++; /* add 1 to one or two scores */
                        if (q >= p) { count++; goto cont; }

                        /* determine if p reached by surprising score */
                        q = t / 3;
                        if (t % 3 != 0) q += t % 3; /* cannot add more */
                        else q++; /* move 1 over; cannot add more */
                        if (q >= p) { surprising_count++; goto cont; }
                cont:
                        //cerr << "max for " << t << " is " << q << endl;
                        continue;
                }
                printf("Case #%d: %d\n", cT, count + min(surprising_count, S));
        }
}
