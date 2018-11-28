#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int empty = 256;
const int maxn = 105;
const int inf = 2147483647/3;
const int base = (1 << 17)-1;
int f[maxn][empty+1],q[base+1][2],a[maxn],head,tail;
bool h[maxn][empty+1];

int calc(int k){
    if (k > 0) return k; return -k;
}

void update(int i,int j,int x,int y,int cost){
    if (f[i][j] + cost < f[x][y]){
        f[x][y] = f[i][j] + cost;
        if (!h[x][y]){
            h[x][y] = true; tail++;
            q[tail&base][0] = x; q[tail&base][1] = y;
        }
    }
}

int main()
{
    freopen("B.in","r",stdin);// freopen("B.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        int cost_D,cost_I,m,n;
        scanf("%d %d %d %d",&cost_D,&cost_I,&m,&n);
        for (int i=1; i<=n; ++i)
            scanf("%d",&a[i]);
        for (int i=0; i<=n+1; ++i)
            for (int j=0; j<=256; ++j)
                f[i][j] = inf;
        memset(h,false,sizeof(h)); h[0][empty] = true;
        f[0][empty] = 0;
        head = 0;tail = 0;
        q[head][0] = 0; q[head][1] = empty;
        while (head <= tail){
            int i = q[head&base][0],j = q[head&base][1];
            if (i == n){
                h[i][j] = false; head++; continue;
            }
            if (j == empty)
                update(i,j,i+1,empty,cost_D);
            else update(i,j,i+1,j,cost_D);
            for (int k=0; k<=255; ++k)
                if (calc(k-j) <= m) update(i,j,i,k,cost_I);
            for (int k=0; k<=255; ++k)
                if (calc(k-j) <= m || j == empty)
                    update(i,j,i+1,k,calc(k-a[i+1]));
            h[i][j] = false; head++;
        }
        int ans = inf;
 /*       for (int i=1; i<=n; ++i)
            for (int j=0; j<=255; ++j)
                printf("(%d %d) %d\n",i,j,f[i][j]); */
        for (int i=0; i<=empty; ++i)
            if (f[n][i] < ans) ans = f[n][i];
        printf("Case #%d: %d\n",casenum,ans);
    }
    return 0;
}
