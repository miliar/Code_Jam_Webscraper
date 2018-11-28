#include <cstdio>
#include <deque>
#include <cstdlib>

using namespace std;
typedef unsigned long long uint64;

int main(int argc, char *argv[]) {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int T;
    int R, K, N;
    uint64 count, euros;
    int i, tmp;    
    deque<int> Q;
    scanf("%d", &T);
    int t = 0;
    while(t < T) {
        scanf("%d %d %d", &R, &K, &N);
        for(int i=0; i<N; ++i) {
            scanf("%d", &tmp);
            Q.push_back(tmp);
        }
        euros = 0ULL;
        int i;
        while(R--) {
            count = 0LLU;
            for(i=0; i<N; ++i) {
                if((count + Q[i]) <= K) {
                    count += Q[i];
                }else{
                    break;
                }                
            }
            if(count == 0) {
                break;
            }
            euros += count;
            for(int j=0; j<i; ++j) {
                Q.push_back(Q.front());
                Q.pop_front();
            }            
        }
        ++t;
        printf("Case #%d: %llu\n", t, euros);
        Q.clear();
    }
    return EXIT_SUCCESS;
}
