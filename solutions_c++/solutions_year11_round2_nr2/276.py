#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
using namespace std;
#define PB push_back

const int INF = 1000000000;
typedef long long LL;
LL a[1010000];
int n, C, D;

bool gao(LL t){
    int i, j, k;
    LL l = -10000000000000000LL;
    for(i = 0; i < n; i++){
        if(l + D < a[i] - t)
            l = a[i] - t;
        else if(l + D - a[i] <= t){
            l = l + D;
        }else
            return false;
    }
    return true;
}

int main(){
    int i, j, k, cas, re;
    freopen("B-large.in", "r", stdin); freopen("w.txt", "w", stdout);
    scanf("%d", &cas);
    for(re = 1; re <= cas; re++){
        printf("Case #%d: ", re);
        scanf("%d%d", &C, &D);
        n = 0;
        for(i = 0; i < C; i++){
            int x, y;
            scanf("%d%d", &x, &y);
            while(y--)
                a[n++] = x * 2;
        }
        D *= 2;
        sort(a, a + n);
        LL l = 0, r = 1000000000000000000LL, m;
        while(l < r){
            m = (l + r) / 2;
            bool flag = gao(m);
            if(flag)
                r = m;
            else
                l = m + 1;
        }
        if(r % 2 == 0)
            printf("%lld\n", r / 2);
        else
            printf("%lld.5\n", r / 2);
    }
}
