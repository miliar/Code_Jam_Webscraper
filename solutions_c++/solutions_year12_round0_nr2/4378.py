#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>
#include <cassert>
#include <cstring>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

int run(int ncase){
    int N, S, p;
    vector<int> scores;
    int i, ans = 0;
    cin >> N >> S >> p;

    scores.resize(N);
    FOR(i, 0, N) {
        cin>> scores[i];
    }
    //cout << N << " " << S << " " << p << endl;
    foreach(scores, itr) {
        int n = *itr;
        int a[3];
        a[0] = a[1] = a[2] = n/3;
        a[2] += (n%3) > 0;
        a[1] += (n%3 - 1) > 0;
        //cout << n << " " << a[0] << " " << a[1] << " " << a[2] << endl;

        if ((a[2] == (p - 1)) && (a[1] == a[2]) && a[1] > 0 && S > 0) {
            S--;
            a[2]++;
            a[1]--;
        }
        //cout << n << " " << a[0] << " " << a[1] << " " << a[2] << endl;
        if (a[2] >= p) ans++;
    }

    cout << "Case #" << ncase << ": ";
    cout << ans << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}
