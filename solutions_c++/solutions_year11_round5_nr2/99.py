#include <stdio.h>
#include <algorithm>
using namespace std;
int a[10010];
int b[10010], c[10010];
int n;
bool f(int x){
    int i, j, t, s;
    for (i = 0; i < 10010; i++){
        b[i] = a[i];
        c[i] = 0;
    }
    for (i = 0; i < 10010; i++){
        if (b[i]){
            break;
        }
    }
    while (i < 10010){
        t = min(c[i], b[i]);
        c[i + 1] += t;
        b[i] -= t;
        s = b[i];
        for (j = x - 1; j >= 0; j--){
            if (b[i + j] < b[i]){
                return false;
            }
            b[i + j] -= b[i];
        }
        c[i + x] += s;
        i++;
        while (i < 10010 && b[i] == 0){
            i++;
        }
    }
    return true;
}
int pd(int l, int r){
    int z = (l + r) / 2;
    if (l + 1 == r){
        return l;
    }
    if (f(z)){
        return pd(z, r);
    }
    return pd(l, z);
}
int main(){
    int T, ri = 1, i, x;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        if (n == 0){
            printf("Case #%d: 0\n", ri++);
            continue;
        }
        memset(a, 0, sizeof(a));
        for (i = 0; i < n; i++){
            scanf("%d", &x);
            a[x]++;
        }
        printf("Case #%d: %d\n", ri++, pd(1, n + 1));
    }
    return 0;
}
