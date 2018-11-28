#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <complex>
#include <numeric>
#include <algorithm>

#include <gmpxx.h>

using namespace std;

#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);i++)

int A[1024];

int main() {
    int T;
    cin >> T;
    FOR(it,1,T+1) {
        int N;
        cin >> N;
        FOR(i,0,N) cin >> A[i];
        int z = 0, mi = INT_MAX, su = 0;
        FOR(i,0,N) {
            z ^= A[i];
            mi = min(mi, A[i]);
            su += A[i];
        }
        cout << "Case #" << it << ": ";
        if(z) {
            cout << "NO";
        } else {
            cout << su - mi;
        }
        cout << endl;
    }
    return 0;
}
