#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int T, R, K, N;
long long G[2000];
long long next[1001], sum[1001], seq[1001], all[1001], len, head;
int pos[1001];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-largex.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d %d %d", &R, &K, &N);
        for(int i=0; i<N; i++){
            scanf("%I64d", &G[i]);
            G[N+i] = G[i];
        }
        for(int i=0; i<N; i++){
            sum[i] = 0; next[i] = i;
            for(int j=i; j<i+N && sum[i]+G[j]<=K; j++){
                next[i] = (j+1)%N;
                sum[i] += G[j];
            }
        }
        memset(pos, -1, sizeof(pos));
        len = 1; head = 0;
        seq[0] = 0; pos[0] = 0;
        for(int i=next[0]; pos[i] == -1; i=next[i]){
            pos[i] = len;
            seq[len++] = i;
            head = pos[next[i]];
        }
        long long tmp = 0;
        for(int i=0; i<head; i++){
            all[i] = tmp+sum[seq[i]];
            tmp = all[i];
        }
        long long fuck = 0;
        tmp = 0;
        for(int i=0; i<len-head; i++){
            fuck += sum[seq[i+head]];
            all[i+head] = tmp+sum[seq[i+head]];
            tmp = all[i+head];
        }
        len -= head;
        long long ans = 0;
        if(R<=head){
            ans = all[R-1];
        } else{
            ans = (head>0)?all[head-1]:0;
            R -= head;
            int tt = R/len, tr = R%len;
            ans += tt*fuck;
            if(tr>0) ans += all[head+tr-1];
        }
        printf("Case #%d: %I64d\n", cas, ans);
    }
    return 0;
}
