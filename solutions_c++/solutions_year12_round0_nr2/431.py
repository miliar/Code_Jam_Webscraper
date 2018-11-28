#include <cstdio>
#include <cstring>

const int MAXS = 31;
const int MAXN = 101;
const int MAXSS = 101;

int T , N , S , P;
int Su[MAXS] , No[MAXS];
int f[MAXN][MAXSS] , num[MAXN];

int max(int x , int y) {
    if (x > y) return x;
    return y;
}

bool    check(int x, int y , int z) {
    int tmp;
    tmp = max(y,z);
    if (tmp - x == 2) return true;
      else return false;
}

void    init() {
    int i , j , k;
    for (i = 0;i <= 10;i++)
      for (j = i;j <= i+2 && j <= 10;j++)
        for (k = i;k <= i+2 && k <= 10;k++)
            if (check(i,j,k)) Su[i+j+k] = max(Su[i+j+k],k);
                else    No[i+j+k] = max(No[i+j+k],k);
}

int main () {
    freopen("dance.in","r",stdin);
    freopen("dance.out","w",stdout);
 
    memset(Su,0,sizeof(Su));
    memset(No,0,sizeof(No));
    init();
    int i , j , k , l;
    scanf("%d\n",&T);
    for (i = 0;i < T;i++) {
        scanf("%d %d %d ",&N,&S,&P);
        for (j = 1;j <= N;j++) scanf("%d\n",&num[j]);
        memset(f,0,sizeof(f));
        for (j = 1;j <= N;j++)
          for (k = 0;k <= S;k++) {
            f[j][k] = f[j-1][k];
            if (No[num[j]] >= P) f[j][k] ++;
            if (k > 0 && f[j-1][k-1] > f[j][k]) f[j][k] = f[j-1][k-1];
            if (Su[num[j]] >= P && k > 0 && f[j-1][k-1]+1 > f[j][k]) f[j][k] = f[j-1][k-1] + 1;
        }
        printf("Case #%d: %d\n",i+1,f[N][S]);
    } 
    return 0;
}
