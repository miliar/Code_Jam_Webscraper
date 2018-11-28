#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int t; scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        int r,k,n; scanf("%d%d%d", &r, &k, &n);
        static int g[1000];
        for(int j = 0; j < n; j++) {
            scanf("%d", g+j);
        }
        int off=0,len=0;
        long long subsum=0;
        static int to[1000];
        static long long tolen[1000];
        for(; off<n;) {
            while(len<n && subsum+g[(off+len)%n]<=k) {
                subsum+=g[(off+len)%n];
                len++;
            }
            to[off]=(off+len)%n;
            tolen[off]=subsum;
            subsum-=g[off];
            off++;len--;
        }
        static long long loop_tim[1000];
        static long long loop_len[1000];
        fill(loop_tim, loop_tim+1000, -1);
        long long cur_tim=0, cur_len=0, cur_at = 0;
        for(; loop_tim[cur_at]==-1 && cur_tim<r; cur_at=to[cur_at]) {
            loop_tim[cur_at]=cur_tim;
            loop_len[cur_at]=cur_len;
            cur_tim++;
            cur_len+=tolen[cur_at];
        }
        long long ret = 0;
        if(cur_tim==r) {
            ret += cur_len;
        } else {
            long long loop_start = loop_len[cur_at];
            long long loop_length = cur_len-loop_len[cur_at];
            long long loop_time = cur_tim-loop_tim[cur_at];
            long long repeat = (r-loop_tim[cur_at])/loop_time;
            long long rem = (r-loop_tim[cur_at])%loop_time;
            ret += loop_start;
            ret += loop_length*repeat;
            for(; rem; rem--) {
                ret += tolen[cur_at];
                cur_at=to[cur_at];
            }
        }
        printf("Case #%d: %lld\n", i+1, ret);
    }
    return 0;
}

