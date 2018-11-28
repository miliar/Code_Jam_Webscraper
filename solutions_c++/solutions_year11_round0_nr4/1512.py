#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>

using namespace std;


int main() {
//    freopen("1.in", "rt", stdin);
    freopen("D-large-1.in", "rt", stdin);
    freopen("D-large-1.out", "wt", stdout);
    int N;
    cin >> N;
    cerr << N;
		for(int nn = 1; nn <= N ; ++nn) {
        cout << "Case #" << nn << ": ";
        int n;
        cin >> n;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
          int k;
          cin >> k;
          if( k != i+1 )
            cnt ++;
        }
        cout << cnt << endl;
    }
    return 0;
}
