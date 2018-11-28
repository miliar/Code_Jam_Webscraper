#include <cstdio>
#include <cstring>

const int MAXN = 2000001;

int  T , A , B , max10 , mb , ms , sum , ans;
bool g[MAXN];

int main () {
    freopen("numbers.in","r",stdin);
    freopen("numbers.out","w",stdout);
    
    int i , j , k , l;
    scanf("%d\n",&T);
    for (i = 0;i < T;i++) {
        scanf("%d %d\n",&A,&B);
        memset(g,false,sizeof(g));
        printf("Case #%d: ",i+1);
        max10 = 1;
        ans = 0;
        for (int tmp = A;tmp > 0;tmp/=10,max10*=10);
        max10/=10;
        for (j = A;j <= B;j++)
          if (!g[j]) {
             g[j] = true;
             mb = max10; ms = 10;
             sum = 1;
             while (ms<j) {
                k = (j%ms)*mb+j/ms;
                if (k>=A && k<=B && !g[k]) {
                    g[k] = true;
                    sum ++;
                }
                ms *= 10; mb /= 10;
            }
            ans += sum*(sum-1)/2;
        }
        printf("%d\n",ans);
    }
    return 0;
}
