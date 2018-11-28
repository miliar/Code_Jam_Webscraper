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

int A[1024], B[1024];

int main() {
    int T;
    cin >> T;
    FOR(it,1,T+1) {
        int N;
        cin >> N;
        FOR(i,0,N) cin >> A[i];
        memcpy(B,A,sizeof(B));
        sort(B,B+N);
        double res = 0;
        FOR(i,0,N) res += (A[i] != B[i]);
        cout << "Case #" << it << ": " << fixed << setprecision(6) << res << endl;
    }
    return 0;
}
