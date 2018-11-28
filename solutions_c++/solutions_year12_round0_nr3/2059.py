#include <cstdio>
using namespace std;
#define MAX 2000001
#define LL long long

LL sum;
bool t[MAX];

int f(int a)
{
    int k = 0;
    while(a){
        ++ k;
        a /= 10;
    }
    return k;
}

int npok(int n)
{
    if(n <= 1) return 0;
    if(n == 2) return 1;
    if(n == 3) return 3;
    if(n == 4) return 6;
    if(n == 5) return 10;
    if(n == 6) return 15;
    if(n == 7) return 21;
    if(n == 8) return 28;
}

void check(int a, int l, int p, int k)
{
    int h = l, ile=0, pot = 1;
    while(-- h) pot*= 10;
    h=l;
    while(h --){
        if(a < MAX) if(!t[a] && a <= k){ t[a] = 1;
        if(a <= k && a >= p) ++ ile;}
        int j = a%10;
        a /= 10;
        a += pot* j;
    }
    sum += npok(ile);
}

void czysc(int k)
{
    for(int i = 0; i <= k; ++ i)
        t[i] = 0;
    sum = 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int o = 1; o <= n; ++ o){
        int a, b;
        scanf("%d %d", &a, &b);
        int k = f(a);
        for(int i = a; i <= b; ++ i)
            if(!t[i]) check(i, k, a, b);
        printf("Case #%d: %lld\n", o, sum);
        czysc(b);
    }
}
