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

const int maxn = 10240;

int n, D;
int d[maxn], l[maxn];
int dyn[maxn];

int main()
{
    freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);

    int i, j, k;
    
    int T, sc;
    cin >> T;
    for (sc = 0; sc < T; sc++) {
        scanf("%d", &n);
        for (i = 1; i <= n; i++) {
            scanf("%d%d", &d[i], &l[i]);
        }
        d[0] = 0;
        scanf("%d", &D);

        memset(dyn, 0xff, sizeof(dyn));
        dyn[1] = 0;
        for (i = 1; i < n; i++) {
            if (dyn[i] == -1) continue;
            for (j = i+1; j <= n; j++) {
                if (d[j] > 2*d[i]-dyn[i]) break;
                int cur_pos = max(d[j]-l[j], d[i]);
                if (dyn[j] < 0 || cur_pos < dyn[j])
                    dyn[j] = cur_pos;
            }
        }

        int ok = 0;
        for (i = 1; i <= n; i++) {
            if (dyn[i] != -1 && 2*d[i]-dyn[i] >= D)
                ok = 1;
        }

        cout << "Case #" << sc+1 << ": ";
        cout << (ok ? "YES" : "NO");
        cout << endl;
    }
    
    
    fclose(stdin); fclose(stdout);
    return 0;   
}
