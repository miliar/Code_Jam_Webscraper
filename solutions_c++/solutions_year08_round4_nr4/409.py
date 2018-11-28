#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int P[20];
int N, K;
char S[1024];
int BEST;

int main() {
    scanf("%d", &N);
    for (int cix=0; cix<N; cix++) {
        scanf("%d", &K);
        scanf("%s", S);
        
        for (int i=0; i<K; i++) P[i]=i;
        BEST=999999;
        int L=strlen(S);
        do {
            char last='*'; int cnt=0;        
            for (int i=0; i<L; i++) {
                char curr=S[P[i%K]+K*(i/K)];
                //printf("%c", curr);
                if (last!=curr) cnt++;
                last=curr;
                }
            if (cnt<BEST) BEST=cnt;
            //printf(" %d\n", cnt);
        } while (next_permutation(P, P+K));
        
        printf("Case #%d: %d\n", cix+1, BEST);        
    }
    return 0;
}
