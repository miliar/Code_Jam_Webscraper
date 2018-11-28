#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <map>
#include <utility>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <numeric>
#include <set>
#include <sstream>
#include <list>
#include <cassert>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long int ll;
typedef vector<ll> vl;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int L, P, C;
        cin >> L >> P >> C;
        int n = ceil(log((P+0.0)/(L+0.0))/log(C));
        int res = ceil(log(n)/log(2.0));
        // cerr << "L=" << L << " P=" << P << " C=" << C << " n=" << n << " res=" << res << "\n";
        cout << "Case #" << cs << ": " << res << "\n";
    }
}
