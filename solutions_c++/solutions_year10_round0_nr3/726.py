#include <cstdio>

const long long N = 1010;

long long g[N]={};
bool visit[N]={};

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.out","w",stdout);

    long long t, cas = 0, r, k, n;
    scanf("%I64d", &t);
    while (t--){
        scanf("%I64d %I64d %I64d", &r, &k, &n);
        for (long long i = 0; i < n; ++i){
            scanf("%I64d", &g[i]);
            visit[i] = 0;
        }
        long long ans = 0;
        long long pos = 0, cnt;
        while (r){
            if (!visit[pos]){
                visit[pos] = 1;
                cnt = 0;
                long long start = pos;
                while ((long long)cnt + g[pos] <= k){
                    cnt += g[pos];
                    pos = (pos+1)%n;
                    if (pos == start) break;
                }
                ans += cnt;
                --r;
            }
            else{
                long long round = 0, income = 0, p = pos;
                do{
                    cnt = 0;
                    long long start = p;
                    while ((long long)cnt + g[p] <= k){
                        cnt += g[p];
                        p = (p+1)%n;
                        if (p == start) break;
                    }
                    income += cnt;
                    ++round;
                }while (p != pos);
                ans += ((long long)r/round)*income;
                r %= round;
                for (long long i = 0; i < n; ++i) visit[i] = 0;
            }
        }
        printf("Case #%I64d: %I64d\n", ++cas, ans);
    }
    return 0;
}
