#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int f[3][200], n, m, p;
int g[200];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T; cin >> T;
    for (int o = 1; o <= T; o++){
        printf("Case #%d: ", o);
        cin >> n >> m >> p;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 105; j++) f[i][j] = -1000;
        f[0][0] = f[1][0] = f[2][0] = 0;
        for (int i = 0; i < n; i++){
            int k;
            cin >> k; int q = k % 3;
            if (q == 0){
                memcpy(g, f[q], sizeof(g));
                if (k / 3 >= p)
                for (int j = 0; j < 105; j++)
                    f[q][j] = g[j] + 1;
                if (k >= 3 && k / 3 + 1 >= p)
                for (int j = 1; j < 105; j++)
                    f[q][j] = max(f[q][j], g[j-1] + 1);
              //  if (k >= 3 && k / 3 + 1 < p)
               // for (int j = 1; j < 105; j++)
                 //   f[q][j] = max(f[q][j], g[j-1]);
            } else
            if (q == 1){
                memcpy(g, f[q], sizeof(g));
                if (k / 3 + 1 >= p)
                for (int j = 0; j < 105; j++)
                    f[q][j] = g[j] + 1;
            } else {
                memcpy(g, f[q], sizeof(g));
                if (k / 3 + 1 >= p)
                for (int j = 0; j < 105; j++)
                    f[q][j] = g[j] + 1;
                if (k / 3 + 2 >= p)
                for (int j = 1; j < 105; j++)
                    f[q][j] = max(f[q][j], g[j-1] + 1);
                  //  else
              //  for (int j = 1; j < 105; j++)
                  //  f[q][j] = max(f[q][j], g[j-1]);
            }
        }

        int ans = 0;
        for (int a = 0; a <= m; a++)
            for (int b = 0; b <= m ; b++)
                for (int c = 0; c <= m; c++)
                    if (a + b + c <= m) ans = max(ans , f[0][a] + f[1][b] + f[2][c]);
        cout << ans << endl;
    }
}
