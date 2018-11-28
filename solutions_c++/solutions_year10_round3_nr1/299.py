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
        int N;
        cin >> N;
        vl a(N), b(N);
        for (int n=0; n<N; ++n)
            cin >> a[n] >> b[n];
        ll res=0;
        for (int i=0; i<N-1; ++i) 
            for (int j=i+1; j<N; ++j)
                if ((a[j] - a[i])*(b[j] - b[i]) < 0)
                    ++res;
        cout << "Case #" << cs << ": " << res << "\n";
    }
}
