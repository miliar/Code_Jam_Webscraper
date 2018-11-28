#include <cstdlib>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
#define FOR(i, n) for(int i=0; i<n; ++i)
#define FORV(i, v) for(int i=0; i<v.size(); ++i)
#define INF 2147483647

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    FOR(p, T) {
        bool M[2][101][101];
        int n, x1, x2, y1, y2, kol = 1, res = 0, flag = 0;
        memset(M, 0, sizeof(M));
        cin >> n;
        FOR(i, n) {
            cin >> x1 >> y1 >> x2 >> y2;
            for(int j=x1; j<=x2; ++j)
                for(int k=y1; k<=y2; ++k)
                    M[0][j][k] = true;
        }
        
        while(kol>0) {
            kol = 0;
            res++;
            for(int i=1; i<=100; ++i)
                for(int j=1; j<=100; ++j)
                    if(M[flag][i][j]) {
                        if(M[flag][i-1][j] || M[flag][i][j-1]) {M[(flag+1)%2][i][j] = true; kol++;}
                        else M[(flag+1)%2][i][j] = false;
                    }
                    else {
                        if(M[flag][i-1][j] && M[flag][i][j-1]) {M[(flag+1)%2][i][j] = true; kol++;}
                        else M[(flag+1)%2][i][j] = false;
                    }
            memset(M[flag], 0, sizeof(M[flag]));  
            flag = (flag+1)%2;
        }
        cout << "Case #" << p+1 << ": " << res << endl;
    }
    
    return 0;
}
