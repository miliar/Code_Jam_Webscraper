#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define oo 1e9
#define eps 1e-8

using namespace std;

int m, n, T, t, ma, mi, q, w, e, r, an, s;
char a[100][100], temp[10];
bool ok;

int main(){
    scanf("%d", &T);
    for (int rr = 1; rr <= T; rr++){
        memset(a, 0, sizeof(a));
        printf("Case #%d:\n", rr);
        scanf("%d%d", &m, &n);
        gets(temp);
        for (int i=0; i<m; i++)
        gets(a[i]);
        ok = true;
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
                if (a[i][j] == '#'){
                   if (a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#'){
                      a[i][j] = '/'; a[i+1][j] = '\\'; a[i][j+1] = '\\'; a[i+1][j+1] = '/';              
                   } else{
                   ok = false;
                   break;
                   }
                            
                }
        if (ok == false)
           puts("Impossible");
        else
        for (int i=0; i<m; i++)
            puts(a[i]);                
    }
}
