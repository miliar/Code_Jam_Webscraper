#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int dyn[10][1024];
int price[1024];
int M[1024];
int inf = 500*1000*1000;

int P, twoP;

int go(int mis, int n)
{
    //printf("go(%d, %d)\n", mis, n);
    if (n >= twoP)
        return mis > M[n - twoP] ? inf : 0;
    int &d = dyn[mis][n];
    if (d >= 0)
        return d;
    d = min(inf, min(go(mis+1, n*2)+go(mis+1,n*2+1),go(mis,n*2)+go(mis,n*2+1)+price[n]));
    //printf("go(%d, %d) -> %d\n", mis, n, d);
    return d;
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int t = 1 ; t <= T ; t++)
        {
            memset(dyn, -1, sizeof(dyn));
            memset(price, 0, sizeof(price));
            scanf("%d", &P);
            twoP = 1 << P;
            for (int i = twoP - 1 ; i >= 0 ; i--)
                scanf("%d", &M[i]);
            for (int i = twoP - 1 ; i > 0 ; i--)
                scanf("%d", &price[i]);
            printf("Case #%d: %d\n", t, go(0, 1));
        }
}
