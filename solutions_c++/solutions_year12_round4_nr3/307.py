#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>

const int maxn = 11;
const int max_val = 1000000000;

int p[maxn], y[maxn];

inline int checkok(int i, int j)
{
    TT L = (y[j]-(TT)y[i])*(p[i]-i);
    TT R = (y[p[i]]-(TT)y[i])*(j-i);
    if (j < p[i]) {
        return L < R;
    } else {
        return L <= R;
    }
}

int main()
{
    freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
    
    int T, sc;
    cin >> T;
    for (sc = 0; sc < T; sc++) {
        int i, j, k, n;
        cin >> n;
        for (i = 0; i < n-1; i++) {
            cin >> p[i];
            p[i]--;
        }

        bool sol = false;
        for (int tries = 0; tries < 1000000; tries++) {
            for (i = 0; i < n; i++) {
                y[i] = (rand()*rand() + rand()) % max_val;
            }
            bool ok = true;
            for (int rep = 0; rep < 10; rep++) {
                bool ch = false;
                for (i = 0; i < n-1; i++) {
                    if (p[i] <= i) {
                        ok = false;
                        break;
                    }
                    for (j = i+1; j < n; j++) {
                        if (j == p[i]) continue;
                        if (!checkok(i, j)) {
                            y[j] = y[i] + (y[p[i]]-y[i]) * ((j-i) / (double)(p[i]-i));
                            ch = true;
                            if (!checkok(i, j)) {
                                y[j]--;
                            }
                            if (y[j] < 0) {ok = false; break;}
                        }
                    }
                    if (!ok) break;
                }
                if (!ok) break;
                if (!ch) break;
            }
            for (i = 0; i < n-1; i++) {
                for (j = i+1; j < n; j++) {
                    if (j == p[i]) continue;
                    if (!checkok(i, j)) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) break;
            }
            if (ok) {
                sol = true;
                break;
            }
        }

        cout << "Case #" << sc+1 << ": ";
        if (sol) {
            for (i = 0; i < n; i++)
                cout << y[i] << " ";
        } else cout << "Impossible";
        cout << endl;
    }
    
    
    fclose(stdin); fclose(stdout);
    return 0;   
}
