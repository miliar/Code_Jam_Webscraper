#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve(int x) {
    int N,i,j;
    float wm[111] = {}, m[111] = {},wp[111],owp[111],oowp[111];
    char f[111][111];
    cin >> N;
    fgets(f[1],N,stdin);
    for (i = 1; i <= N; i++) { 
        gets(f[i]);
        };
    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N; j++) {
            if (f[i][j-1] == '.') continue;
            m[i] = m[i] + 1;
            if (f[i][j-1] == '1') wm[i] = wm[i] + 1;
        }
        wp[i] = wm[i]/m[i] * 1.0;
    }
    for (i = 1; i <= N; i++) {
        float tw = 0;
        for (j = 1; j <= N; j++) {
            if (f[j][i-1] == '.') continue;
            if (f[j][i-1] == '0') tw = tw + (wm[j]/(m[j]-1));
            else tw = tw + (wm[j]-1)/(m[j]-1);            
        }
        owp[i] = tw/ m[i];
    }
    for (i = 1; i <= N; i++) {
        float tw = 0;
        for (j = 1; j <= N; j++) {
            if (f[i][j-1] == '.') continue;
            tw = tw + owp[j];
        }
        oowp[i] = tw/m[i];
    }
    cout<<"Case #"<<x<<":\n";
    for (i = 1;i <= N; i++) cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]<<"\n";
}


int main() {
    
    freopen("A-large.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    int t,i,j;
    cin >> t;
    for (i = 1;i <= t; i++) {
        solve(i);
    }
}
