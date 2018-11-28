#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int MAXN = 120;
bool v[MAXN][MAXN];
int t, n;
bool vv[MAXN][MAXN];
int xx1, yy1, xx2, yy2;

int main(){
    int t;
    freopen("C.in","r",stdin);
    freopen("C.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i){
        scanf("%d",&n);
        printf("Case #%d: ",i);
        memset(v, 0, sizeof(v));
        for (int j = 0; j < n; ++j){
            scanf("%d%d%d%d",&xx1, &yy1, &xx2, &yy2);
            --xx1;
            --yy1;
            --xx2;
            --yy2;
            for (int p = yy1; p <= yy2; ++p)
                for (int q = xx1; q <= xx2; ++q)
                   v[p + 5][q + 5] = true;
        }

        int tot = 0;
        for (int j = 0; j < 110; ++j)
            for (int k = 0; k < 110; ++k)
                if (v[j][k]) tot++;
        int ans = 0;
        
        if (tot == 0) printf("0\n");
        else{
            while (true){
                 ans++;  
                 memset(vv, 0, sizeof(vv));
                 for (int j = 0; j < 110; ++j) for (int k = 0; k < 110; ++k) vv[j][k] = v[j][k];
                 
                 for (int j = 0; j < 110; ++j)
                     for (int k = 0; k < 110; ++k)
                         if (!v[j - 1][k] && !v[j][k - 1] && v[j][k]) vv[j][k] = false;
                         else if (v[j - 1][k] && v[j][k - 1] && !v[j][k]) vv[j][k] = true;
            
                 tot = 0;
                 for (int j = 0; j < 110; ++j)
                    for (int k = 0; k < 110; ++k)
                        if (vv[j][k]) tot++;
                 
                 if (tot == 0){
                     printf("%d\n",ans);
                     break;
                 }
                 for (int j = 0; j < 110; ++j)
                    for (int k = 0; k < 110; ++k) v[j][k] = vv[j][k];
            }
        }
    }
    return 0;
}
