#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool bit(int64 mask, int k) {
    return ((1LL << k) & mask) != 0;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        
        int n, m;
        cin >> n >> m;
        vector<string> table(n);
        for (int i = 0; i < n; ++i) {
            cin >> table[i];
        }
        int di[8] = {0, 1, 0, -1, 1, 1, -1, -1};
        int dj[8] = {1, 0, -1, 0, 1, -1, 1, -1};

        int64 res = 0;
        vvi mm(n, vi(m));
        for (int64 mask = 0; mask < (1LL << (n * m)); ++mask) {
            for (int i =0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    bool b = bit(mask, i * m + j);
                    switch(table[i][j]) {
                        case '-':
                            mm[i][j] = b ? 0 : 2;
                            break;
                        case '|':
                            mm[i][j] = b ? 1 : 3;
                            break;
                        case '/':
                            mm[i][j] = b ? 5 : 6;
                            break;
                        case '\\':
                            mm[i][j] = b ? 4 : 7;
                            break;
                    }
                }
            }
            bool ok = true;
            for (int i =0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    int c = 0;
                    for (int k = 0; k < 8; ++k) {
                        int i1 = (i + di[k] + n) % n;
                        int j1 = (j + dj[k] + m) % m;
                        int k1 = mm[i1][j1];
                        int i2 = (i1 + di[k1] + n) % n;
                        int j2 = (j1 + dj[k1] + m) % m;
                        if (i2 == i && j2 == j) ++c;
                    }
                    ok &= c == 1;
                    if (!ok) break;
                }
                if (!ok) break;
            }
            if (ok) ++res;
        }
        res %= 1000003;

        /*printf("Case #%d:\n", testNumber);
        for (int i = 0; i < sz(res); ++i) {
            printf("%.8lf\n", res[i]);
        }*/
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}

//#include <stdio.h>
//#include <iostream>
//#include <vector>
//#include <string>
//#include <math.h>
//#include <algorithm>
//#include <bitset>
//#include <set>
//#include <sstream>
//#include <stdlib.h>
//#include <map>
//#include <queue>
//#include <assert.h>
//
//using namespace std;
//
//#define sz(x) ((int)x.size())
//#define all(x) (x).begin(), (x).end()
//#define pb(x) push_back(x)
//#define mp(x, y) make_pair(x, y)
//
//#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)
//
//#define debug(x) cout << '>' << #x << ':' << x << endl;
//
//typedef long long int64;
//
//typedef vector <int> vi;
//typedef vector < vi > vvi;
//
//bool bit(int64 mask, int k) {
//    return ((1LL << k) & mask) != 0;
//}
//
//int di[] = {0, -1, -1, -1, 0, 1, 1, 1};
//int dj[] = {1, 1, 0, -1, -1, -1, 0, 1};
//
//int get(char c, bool b) {
//    switch (c) {
//        case '-':
//            return b ? 0 : 4;
//        case '|':
//            return b ? 2 : 6;
//        case '/':
//            return b ? 1 : 5;
//        case '\':
//            return b ? 3 : 7;
//    }
//    return -1;
//}
//
//int main() {
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
//    
//    int testCount;
//    cin >> testCount;
//    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
//        cerr << "Case #" << testNumber << "..." << endl;
//        
//        int n, m;
//        cin >> n >> m;
//        vector<string> table(n);
//        for (int i = 0; i < n; ++i) {
//            cin >> table[i];
//        }
//        
//        for (int64 mask = 0; mask < (1LL << (n * m)); ++mask) {
//            vvi use(n, vi(m));
//            for (int i = 0; i < n; ++i) {
//                for (int j = 0; j < m; ++j) {
//                    int k = get(table[i][j], bit(mask, m * i + j
//                }
//            }
//        }
//        res %= 1000003;
//
//        /*printf("Case #%d:\n", testNumber);
//        for (int i = 0; i < sz(res); ++i) {
//            printf("%.8lf\n", res[i]);
//        }*/
//        cout << "Case #" << testNumber << ": " << res << endl;
//    }
//
//    return 0;
//}