#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define oo 1e9
#define eps 1e-8

using namespace std;

int m, n, T, t, ma, mi, q, w, e, r, an, s, l, h;
int a[200];
bool ok;

int main(){
    scanf("%d", &T);
    for (int rr = 1; rr <= T; rr++){
        printf("Case #%d: ", rr);
        scanf("%d%d%d", &n, &l, &h);
        for (int i=0; i<n; i++)
            scanf("%d", &a[i]);
        an = 0;
        for (int i=l; i<=h; i++){
            ok = true;
            for (int j=0; j<n; j++)
                if (i % a[j] != 0 && a[j]%i != 0){
                   ok = false;
                   break;
                }
            if (ok){
               an = i;
               break;
            }
        }
        if (ok)
           printf("%d\n", an);
        else printf("NO\n");
        
    }
}
