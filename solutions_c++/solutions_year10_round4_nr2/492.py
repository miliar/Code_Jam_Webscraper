#include <stdio.h>
#include <cstring>

const int MAXVAL = 500000000;

inline int min(int a, int b){
    return (a < b) ? a : b;
}

int f[2048][11];
int N[2048], tot;

int calc(int n, int a){
    if(f[n][a] >= 0)
        return f[n][a];
    if(n >= tot)
        return MAXVAL;
    int ret = MAXVAL;
    int x = calc(n << 1, a + 1);
    int Y = calc((n << 1) | 1, 0);
    for(int i = 1;i <= a;i++)
        Y = min(Y, calc((n << 1) | 1, i));
    int X = calc(n << 1, 0);
    for(int i = 1;i <= a;i++)
        X = min(X, calc(n << 1, i));
    int y = calc((n << 1) | 1, a + 1);
    int z0 = calc(n << 1, a);
    int z1 = calc((n << 1) | 1, a);
    ret = min(ret, x + Y + N[n]);
    ret = min(ret, X + y + N[n]);
    ret = min(ret, x + y + N[n]);
    ret = min(ret, z0 + Y);
    ret = min(ret, X + z1);
    f[n][a] = ret;
    return ret;
}

int main(){
    int testnum, p, temp;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        memset(f, 0xff, sizeof(f));
        scanf("%d", &p);
        tot = 1 << p;
        for(int i = tot;i < (tot << 1);i++){
            scanf("%d", &temp);
            f[i][p - temp] = 0;
        }
        temp = tot >> 1;
		//printf("temp:%d tot:%d\n", temp, tot);
        while(temp){
            for(int i = temp;i < (temp << 1);i++){
                scanf("%d", &N[i]);
            }
            temp >>= 1;
        }
        printf("Case #%d: %d\n", test, calc(1, 0));
    }
    return 0;
}
