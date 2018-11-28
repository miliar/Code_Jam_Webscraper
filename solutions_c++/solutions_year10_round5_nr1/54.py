#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int limit = 1000005;
bool prime[limit],zero[15];
int p[100000],s[15],a[15][15],b[15],x[15];
int n,m,base,pre,now,last;
bool yes,ok;

int calc(int k){
    return (k%base + base) % base;
}

void search(int r,int c){
    if (!yes) return;
    if (r == 0){
        now = (last % base * x[1] % base + x[2]) % base;
        ok = true;
        if (pre != -1 && now != pre){
            yes = false; return;
        }
        pre = now;
        return;
    }
    if (zero[c]){
        for (x[c] = 0; x[c] < base; ++x[c])
            search(r,c-1);
    } else {
        int tmp = 0;
        for (int i=c+1; i<=m; ++i) tmp = calc(tmp + a[r][i] * x[i]);
        for (x[c] = 0; x[c] < base; ++x[c])
            if (calc(x[c] * a[r][c] + tmp) == calc(b[r]))
                search(r-1,c-1);
    }
}

bool Gauss(){
    memset(zero,false,sizeof(zero));
    int r = 1,c = 1;
    while (r <= n && c <= m){
        if (a[r][c] == 0){
            int k = r,tmp;
            for (int i=r+1; i<=n; ++i)
                if (a[i][c]){
                    k = i; break;
                }
            if (r != k){
                for (int i=c; i<=m; ++i){
                    tmp = a[r][i]; a[r][i] = a[k][i]; a[k][i] = tmp;
                }
                tmp = b[r]; b[r] = b[k]; b[k] = tmp;
            } else {
                zero[c] = true; c++; continue;
            }
        }
        for (int i=r+1; i<=n; ++i)
            while (a[i][c]){
                if (a[r][c] > a[i][c]){
                    for (int j=c; j<=m; ++j)
                        a[r][j] = calc(a[r][j] - a[i][j]);
                    b[r] = calc(b[r] - b[i]);
                } else{
                    for (int j=c; j<=m; ++j)
                        a[i][j] = calc(a[i][j] - a[r][j]);
                    b[i] = calc(b[i] - b[r]);
                }
            }
        r++; c++;
    }
    for (int i=r; i<=n; ++i) if (b[i]) return false;
    search(r-1,c-1);
    return yes;
}

int main()
{
    freopen("A.in","r",stdin); freopen("A.out","w",stdout);
    memset(prime,true,sizeof(prime));
    prime[1] = false; prime[0] = false;
    for (int i=2; i<limit; ++i)
        if (prime[i]){
            for (int j=i; j <= limit/i; ++j)
                prime[i*j] = false;
        }
    int t = 0;
    for (int i=2; i<limit; ++i)
        if (prime[i]) p[++t] = i;
    int c; scanf("%d",&c);
    for (int casenum=1; casenum <= c; ++casenum){
        int d,tmp,k; scanf("%d %d",&tmp,&k);
        d = 1;
        for (int i=1; i<=tmp; ++i)
            d *= 10;
        int up = 0;
        for (int i=1; i<=k; ++i){
            scanf("%d",&s[i]); if (s[i] > up) up = s[i];
        }
        ok = false; yes = true;
        pre = -1;
        if (k != 1){
            for (int i=1; i<=t; ++i)
                if (p[i] <= d){
                    if (p[i] <= up) continue;
                    base = p[i];
                    n = 1; m = 2;
                    a[1][1] = s[1] % base; a[1][2] = 1; b[1] = s[2] % base;
                    for (int j=2; j<k; ++j){
                        n++;
                        a[n][1] = s[j] % base; a[n][2] = 1; b[n] = s[n+1] % base;
                    }
                    last = s[k];
                    Gauss();
                    if (ok && !yes) break;
                } else break;
        }
        printf("Case #%d: ",casenum);
        if (ok && yes) printf("%d\n",now);
            else printf("I don't know.\n");
    }
    return 0;
}
