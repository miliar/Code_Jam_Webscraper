#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin>>T;
    int t = 0;
    while (T--) {
        t++;
        int C, D;
        cin>>C>>D;
        double P[200], V[200];
        for (int i=0;i<C;i++) {
            cin>>P[i] >> V[i];
        }

        double low = 0, high = 1e40;
        for (int i=0;i<300;i++) {
            double m = (low + high)/2;
            double p = P[0] - m - D;
            //cout << "Start at " << p << endl;
            int pp = 0;
            int pi = 0;
            bool good = true;
            //cout << "M: " << m << endl;
            while (pi < C && good) {
                double prevP = p;
                p = max(p + D, (double)P[pi] - m);
                //cout << "Try drop " << P[pi] << " at " << p << " moved by " << fabs(p - P[pi]) << endl;
                if (fabs(p - P[pi]) > (m+1e-10)*(1+1e-10)) {
                    good = false;
                    //cout << "Death by dist of " << fabs(p - P[pi]) << endl;
                    break;
                }
                //cout << "Good" << endl;

                pp++;
                if (pp == V[pi]) {
                    pp = 0;
                    pi++;
                }
            }

            if (good) {
                high = m;
            } else {
                low = m;
            }
        }
        cout << "Case #" << t << ": " << low << endl;
    }
}
