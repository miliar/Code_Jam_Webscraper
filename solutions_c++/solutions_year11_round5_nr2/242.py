/*
    2011 Round 3 -
    Dire Straights
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

    int T;
    int N;



    int D[1000];
    int last[1000], len[1000], lastlen;

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        memset(last, 0, sizeof(last));
        memset(len, 0, sizeof(len));
        lastlen = 0;
        scanf("%d", &N);
        for(int i=0; i<N; ++i)
        {
            scanf("%d", &D[i]);
        }
        int ans = 10000;
        sort(D, D+N);
        for(int i=0; i<N; ++i)
        {
            int minlen = 1000, minpos = -1;
            for(int j=0; j<lastlen; ++j)
            {
                if(last[j]+1==D[i] && len[j]<minlen)
                {
                    minlen = len[j];
                    minpos = j;
                }
            }
            if(minpos==-1)
            {
                last[lastlen] = D[i];
                len[lastlen] = 1;
                ++lastlen;
            }
            else{
                ++last[minpos];
                ++len[minpos];
            }
        }
        if(N==0)
        {
            ans = 0;
        }
        else{
            for(int i=0; i<1000; ++i)
            {
                if(len[i]>0 && len[i]<ans)
                {
                    ans = len[i];
                }
            }
        }
        printf("Case #%d: %d\n", z, ans);
    }
    return 0;
}
