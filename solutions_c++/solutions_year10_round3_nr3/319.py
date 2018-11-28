#include <fstream>

using namespace std;

int nr[600][600], n, m, u[600][2], nu;
char s[1024];

int main()
{
    int ok, v, i, j, k, T, x, l, i1, j1;
    ifstream f("c.in");
    ofstream g("c.out");
    f >> T;
    for(x = 1; x <= T; x++){
        nu = 0; u[0][1] = 0;
        f >> n >> m;
        f.get();
        for(i = 0; i < n; i++){
            f >> s;
            for(j = 0; j < m; j+=4){
                if(s[j/4]>= '0'  && s[j/4] <= '9') v = s[j/4] - '0';
                else v = s[j/4] - 'A' + 10;
                for(k = 3; k >= 0; k--){
                    nr[i][j + k] = v % 2;
                    v /= 2;
                }
            }
        }
        for(l = n; l >= 1; l--){
            for(i = 0; i <= n - l; i++)
                for(j = 0; j <= m - l; j++){
                    ok = 1;
                    for(i1 = i+1; i1 < i + l - 1 && ok; i1++)
                        for(j1 = j + 1; j1 < j + l - 1 && ok; j1++){
                            if(nr[i1][j1] == -1) ok = 0;
                            if(nr[i1 + 1][j1] == nr[i1][j1] ||
                                nr[i1][j1 + 1] == nr[i1][j1] ||
                                nr[i1 - 1][j1] == nr[i1][j1] ||
                                nr[i1][j1 - 1] == nr[i1][j1])
                                    ok = 0;
                        }
                    for(j1 = j + 1; j1 < j + l - 1 && ok; j1++){
                        if(nr[i][j1] == -1) ok = 0;
                        if(nr[i][j1-1] == nr[i][j1] || nr[i][j1+1] == nr[i][j1]) ok = 0;
                        if(nr[i+l-1][j1-1] == nr[i+l-1][j1] || nr[i+l-1][j1+1] == nr[i+l-1][j1]) ok = 0;
                    }

                    for(i1 = i + 1; i1 < i + l - 1 && ok; i1++){
                        if(nr[i1][j] == -1) ok = 0;
                        if(nr[i1-1][j] == nr[i1][j] || nr[i1+1][j] == nr[i1][j]) ok = 0;
                        if(nr[i1-1][j+l-1] == nr[i1][j+l-1] || nr[i1+1][j+l-1] == nr[i1][j+l-1]) ok = 0;
                    }
                    if(nr[i][j] == -1 || nr[i][j+l-1] == -1 || nr[i+l-1][j] == -1 || nr[i+l-1][j+l-1] == -1)
                        ok = 0;
                    if(l > 1){
                        if(nr[i][j] == nr[i+1][j] || nr[i][j] == nr[i][j+1]) ok = 0;
                        if(nr[i+l-1][j] == nr[i+l-2][j] || nr[i+l-1][j] == nr[i+l-1][j+1]) ok = 0;
                        if(nr[i][j+l-1] == nr[i+1][j+l-1] || nr[i][j+l-1] == nr[i][j+l-2]) ok = 0;
                        if(nr[i+l-1][j+l-1] == nr[i+l-1][j+l-2] || nr[i+l-1][j+l-1] == nr[i+l-2][j+l-1]) ok = 0;
                    }
                    if(ok){
                        for(i1 = i; i1 < i + l && ok; i1++)
                            for(j1 = j; j1 < j + l && ok; j1++)
                                nr[i1][j1] = -1;
                        u[nu][0] = l; u[nu][1]++;
                    }
                }
                if(u[nu][1]) { nu++; u[nu][1] = 0; }
        }
        g << "Case #" << x << ": " << nu << "\n";
        for(i = 0; i < nu; i++)
            g << u[i][0] << " " << u[i][1] << "\n";
    }
    return 0;
}
