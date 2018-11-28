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

int P[128], V[128];

int main() {
    int T;
    cin >> T;
    FOR(it,1,T+1) {
        int N;
        cin >> N;
        int o = 1, b = 1, lo = 0, lb = 0, r = 0;
        FOR(i,0,N) {
            string bo;
            int po;
            cin >> bo >> po;
            
            if(bo == "O") {
                int cu = lo + abs(po-o) + 1;
                if(cu <= r) cu = r + 1;
                lo = cu;
                o = po;
                r = cu;
            } else {
                int cu = lb + abs(po-b) + 1;
                if(cu <= r) cu = r + 1;
                lb = cu;
                b = po;
                r = cu;
            }
        }
        cout << "Case #" << it << ": "<< r << endl;
    }
    return 0;
}
