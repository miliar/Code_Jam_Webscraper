#include <boost/config.hpp>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <gmp.h>
#include <gmpxx.h>
#include <vector>
#include <boost/utility.hpp>

using namespace std;
using namespace boost;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PI(a,b) make_pair(a,b);

bool arrives(int xi,int vi,int B,int T) {
        return ((long)vi*T + xi >= B);
}

int main() {
    int C;
    cin >> C;
    FOR(i,1,C+1) {
            int N,K,B,T;
            cin >> N >> K >> B >> T;
            vector<int> xi(N);
            FOR(j,0,N) {
                cin >> xi[j];
            }
            vector<int> vi(N);
            FOR(j,0,N) {
                cin >> vi[j];
            }
            int swaps = 0;
            int badhens = 0;
            for (int j = N-1; j >= 0 && K > 0; j--) {
                if (arrives(xi[j],vi[j],B,T)) { K--; swaps += badhens; }
                else badhens++;

                if (K == 0) break;
            }
            cout << "Case #" << i << ": ";
            if (K == 0) cout << swaps;
            else cout << "IMPOSSIBLE";
            cout << endl;
    }
}


