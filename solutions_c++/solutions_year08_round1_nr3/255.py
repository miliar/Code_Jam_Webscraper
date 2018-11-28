#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <ctime>
using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define forit(i, T) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

// const long double term = 3 + sqrt(5.0f);
//const long double t = 5.236067977;

int main()
{
    int T;
    cin >> T;

    vector<string> v(31);

    v[2] = "027"; v[3] = "143"; v[4] = "751"; v[5] = "935";
    v[6] = "607"; v[7] = "903"; v[8] = "991"; v[9] = "335"; v[10] = "047";
    v[11] = "943"; v[12] = "471"; v[13] = "055"; v[14] = "447"; v[15] = "463";
    v[16] = "991"; v[17] = "095"; v[18] = "607"; v[19] = "263"; v[20] = "151";
    v[21] = "855"; v[22] = "527"; v[23] = "743"; v[24] = "351"; v[25] = "135";
    v[26] = "407"; v[27] = "903"; v[28] = "791"; v[29] = "135"; v[30] = "647";

    fori(count,T)
    {
        int n;
        cin >> n;
        cout << "Case #" << count+1 << ": " << v[n] << endl;
    }

    return 0;
}
