#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int maxn = 1000005;

bool f[maxn];
long long p[maxn];

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    memset(f,true,sizeof(f));
    int total = 0;
    for (int i=2; i<maxn; ++i)
        if (f[i]){
            p[++total] = i;
            for (int j=i; j <= maxn / i; ++j)
                f[i * j] = false;
        }
    int T;
    scanf("%d",&T);
    for (int casenum=1; casenum<=T; ++casenum){
        printf("Case #%d: ",casenum);
        long long n;
        cin >> n;
        if (n == 1){
            printf("0\n");
            continue;
        }
        long long ans = 0;
        for (int i=1; i<=total; ++i){
            long long tmp = p[i];
            if (tmp > n) break;
            long long cnt = 0;
            while (tmp <= n){
                cnt++;
                tmp *= p[i];
            }
            ans += cnt - 1;
        }
        ans++;
        cout << ans << endl;
    }
}
