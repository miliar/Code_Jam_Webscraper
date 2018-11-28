
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

ll table[3][1001];
const ll infty = -1;

int main(void)
{
    int t;
    cin >> t;

    for (int prob=1; prob <= t; prob++) {
        ll l, t, n ,c;
        vector<ll> as;
        ll a;

        cin >> l >> t >> n >> c;
       // cerr << "L=" << l << " t=" << t << " n=" << n << " C=" << c << endl;
        for (int i=0; i<c; i++) {
            cin >> a;
            as.push_back(a);
        }

        // init
        table[0][0] = 0;
        table[1][0] = infty;
        table[2][0] = infty;

        for (int next=1; next <= n; next++) {
            for (int nl=0; nl<=l; nl++) {
              // cerr << table[nl][next-1] << " ";
            }
          // cerr << endl;

            ll normal = as[(next-1)%c]*2;
            table[0][next] = table[0][next-1] + normal;

            for (int nl=1; nl<=l; nl++) {
                ll boost;
                ll k = table[nl-1][next-1] + normal;

                if (table[nl-1][next-1] > t) {
                    boost = as[(next-1)%c];
                } else if (k > t) {
                    boost = normal - (k - t)/2;
                } else {
                    boost = normal;
                }

                if (table[nl][next-1] == -1) {
                    if (table[nl-1][next-1] == -1) {
                        table[nl][next] = -1;
                    }
                    else {
                        table[nl][next] = table[nl-1][next-1] + boost;
                    }
                } else {
                    table[nl][next] =  min(table[nl][next-1] + normal, table[nl-1][next-1] + boost);
                }
            }
        }

        for (int nl=0; nl<=l; nl++) {
          // cerr << table[nl][n] << " ";
        }
      // cerr << endl;

        cout << "Case #" << prob << ": " << table[l][n] << endl;
    }

    return 0;
}
