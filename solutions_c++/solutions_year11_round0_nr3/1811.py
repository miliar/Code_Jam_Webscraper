#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
int f[1200];
int main() {
    int cas;
    freopen("a.in", "r", stdin);
    freopen("b1.txt", "w", stdout);
    scanf("%d" ,&cas);

    for (int ccas = 1; ccas <= cas; ++ccas) {
        int t = 0, sum = 0, mins = 100000000;
        scanf("%d", &n);
    
        for (int j = 0; j < n; ++j) {
            scanf("%d", &f[j]); 
            t = t ^ f[j]; 
            sum += f[j]; 
            if (f[j] < mins) mins = f[j]; 
        }
        sum -= mins;       
        
        if (t != 0) printf("Case #%d: NO\n", ccas); else printf("Case #%d: %d\n", ccas, sum);
    }
    return 0;
    
}    
