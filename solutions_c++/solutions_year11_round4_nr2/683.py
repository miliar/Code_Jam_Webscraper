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


using namespace std;


#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define debug(x) cout << '>' << #x << ':' << x << endl;

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)


typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;


int dig(char c) {
    return c - '0';
}



int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int r, c, d;
        cin >> r >> c >> d;
        vector < string > f(r);
        for (int i = 0; i < r; ++i) {
            cin >> f[i];
        }
        
        int ans = 0; 
        for (int k = 2; k + 1 <= min(r, c); ++k) {
            for (int i = 0; i + k < r; ++i) {
                for (int j = 0; j + k < c; ++j) {
                    int sx = 0;
                    int sy = 0;
                    int mass = 0;
                    for (int y = i; y <= i + k; ++y) {
                        for (int x = j; x <= j + k; ++x) {
                            bool sum = true;
                            if (y == i && (x == j || x == j + k)) sum = false;
                            if (y == i + k && (x == j || x == j + k)) sum = false;
                            if (sum) {
                                int m = dig(f[y][x]) + d;
                                sx += x * m;
                                sy += y * m;
                                mass += m;
                            }
                        }
                    }
                    if (( mass * (2 * i + k) == 2 * sy) &&
                        (mass * (2 * j + k) == 2 * sx)) {
                            //cout << "found: " << i << " " << j << " " << k + 1 << endl;
                            ans = max(ans, k + 1);
                        
                        }
                    

                }
            }


        }
        cout << "Case #" << t + 1 << ": ";
        if (ans > 0) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }


    return 0;
}

