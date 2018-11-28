#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

#define DIM 600

int R, C, D;
int w[DIM][DIM];
int pref[DIM][DIM];
char buf[DIM];

int getsum(int i1, int j1, int i2, int j2) {
   int res = pref[i2][j2];
   if (i1 > 0) {
       res -= pref[i1-1][j2];
   }
   if (j1 > 0) {
       res -= pref[i2][j1 - 1];
   }
   if (i1 > 0 && j1 > 0) {
       res += pref[i1 - 1][j1 - 1];
   }
   return res;
}

/*
double colsum[DIM];

bool check(int k) {
    cout << "check " << k << endl;
    for (int i = 0; i + k <= R; ++i) {

        int i2 = i + k - 1;
        int j2 = j + k - 1;

        cout << "row " << i << endl;

        for (int j = 0; j < C; ++j) {
            colsum[j] = getsum(i, j, i2, j);
            cout << "\t" << j << ": " << colsum[j];
        }

        for (int j = 0; j + k <= C; ++j) {
            double 
        }
    }
}
*/

inline int getc(int x, int k) {
    if (k & 1) {
        return x - (k-1)/2;
    } else {
        if (x < k/2) {
            return x - k/2;
        } else {
            return (x+1) - k/2;
        }
    }
}

bool check(int k) {
   //cout << "cur k = " << k << endl;
   for (int i = 0; i + k <= R; ++i) {
       for (int j = 0; j + k <= C; ++j) {
           double rsum, csum;

           double totsum = getsum(i, j, i+k-1, j+k-1) - w[i][j] - w[i+k-1][j+k-1] - w[i+k-1][j] - w[i][j+k-1];
           
           rsum = csum = 0;
           double mid = k / 2.0;
           for (int x = 0; x < k; ++x) {
               int crsum = getsum(i + x, j, i + x, j + k - 1);
               if (x == 0 || x == k-1) {
                   crsum -= w[i+x][j];
                   crsum -= w[i+x][j+k-1];
               }
               rsum += getc(x,k) * crsum;

               int ccsum = getsum(i, j + x, i + k - 1, j + x);
               if (x == 0 || x == k-1) {
                   ccsum -= w[i][j+x];
                   ccsum -= w[i+k-1][j+x];
               }

               csum += getc(x,k) * (ccsum);
           }

           //cout << totsum << endl;
           //cout << i << ", " << j << ": " << "(" << rsum << ", " << csum << ")\n";
           if (csum == 0 && rsum == 0) {
               return true;
           }
       }
   }
   return false;
}

int solve() {
    /*
    int left = 3;
    int right = min(R, C);
    int res = -1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (check(mid)) {
            res = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    */
    for (int k = min(R, C); k >= 3; --k) {
        if (check(k)) {
            return k;
        }
    }
    return -1;
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int numTests;
    scanf("%i\n", &numTests);
    for (int nt = 1; nt <= numTests; ++nt) {
        scanf("%i%i%i\n", &R, &C, &D);
        for (int i = 0; i < R; ++i) {
            gets(buf);
            for (int j = 0; j < C; ++j) {
                w[i][j] = (buf[j] - '0');
            }
        }

        for (int i = 0; i < R; ++i) {
            int curpref = 0;
            for (int j = 0; j < C; ++j) {
                curpref += w[i][j];
                pref[i][j] = curpref;
                if (i > 0) {
                    pref[i][j] += pref[i-1][j];
                }
                //cout << i << ", " << j << ": " << pref[i][j] << endl;
            }
        }

        int res = solve();

        cout << "Case #" << nt << ": ";
        if (res != -1) {
            cout << res << endl;
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    
    return 0;
}