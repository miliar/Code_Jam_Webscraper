#include <cstdio>

int main(int argc, char **argv) {
    int tc; scanf("%d", &tc);
    for(int tci = 0; tci < tc; tci++) {
        int l,p,c; scanf("%d%d%d", &l, &p, &c);
        //printf("l=%d,p=%d,c=%d\n",l,p,c);
        int cnt0 = 0;
        for(long long x = l; x < p; x*=c) {
            cnt0++;
        }
        //printf("cnt0=%d\n",cnt0);
        cnt0--;
        int cnt1 = 0;
        while(cnt0){cnt0>>=1;cnt1++;}
        printf("Case #%d: %d\n",tci+1,cnt1);
        fflush(stdout);
    }
    return 0;
}

