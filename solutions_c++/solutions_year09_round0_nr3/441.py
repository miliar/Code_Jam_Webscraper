#include <stdio.h>
#include <cstring>

const int mod = 10000;

char* a;
char b[512];
int f[20][512];

int calc(int x, int y){
    if(x < 0)
        return 1;
    if(y < 0)
        return 0;
    if(f[x][y] >= 0)
        return f[x][y];
    int res = calc(x, y - 1);
    if(a[x] == b[y])
        res += calc(x - 1, y - 1);
    return (f[x][y] = res % mod);
}

int main(){
    int testnum, ret;

    a = "welcome to code jam";
    scanf("%d", &testnum);
    gets(b);
    for(int test = 1;test <= testnum;test++){
        memset(f, 0xff, sizeof(f));
        gets(b);
        printf("Case #%d: ", test);
        ret = calc(18, strlen(b) - 1);
        if(ret < 1000) putchar('0');
        if(ret < 100) putchar('0');
        if(ret < 10) putchar('0');
        printf("%d\n", ret);
    }
    return 0;
}
