#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP(a,b) make_pair(a,b)


int main (void) {
    int T;
    cin >> T;
    REP(i, T) {
        int N;
        cin >> N;
        int minValue = 10000000;
        int sum = 0;
        int exor = 0;
        REP(j, N) {
            int tmp;
            cin >> tmp;
            minValue = min<int>(tmp, minValue);
            sum += tmp;
            exor ^= tmp;
        }
        if (exor != 0) {
            cout << "Case #" << (i + 1) << ": NO" << endl;
        } else {
            cout << "Case #" << (i + 1) << ": " << (sum - minValue) << endl;
        }
    }
    return 0;
}
