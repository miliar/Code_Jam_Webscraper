#include <boost/config.hpp>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
#include <cmath>
#include <gmp.h>
#include <gmpxx.h>
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
#define PI(a,b) (make_pair(a,b));

typedef long long ll;


int main() {
    int T;
    cin >> T;
    FOR(i,1,T+1) {
            long long L,P,C;
            cin >> L >> P >> C;
            ll k = ceil(log(((long double)(P))/(long double)L) / log((long double) C));
            ll result = 0;
            if (k >= 1) result = ceil(log(k)/log(2));
            cout << "Case #" << i << ": "  << result <<  endl;

    }
}


