#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
using namespace std;
#define ll long long
#define MAX_LETTERS 1001

long long freq[MAX_LETTERS];

int main(){
    int TC;
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        int P, K, L;
        scanf("%d%d%d", &P, &K, &L);
        for(int i = 0; i < L; ++i){
            scanf("%lld", &freq[i]);
        }
        sort(freq, &freq[L], greater<int>());
        //for(int i = 0; i < L; ++i)
        //    printf("%d ", freq[i]);
        //printf("\n");
        long long result = 0, iter = 0;
        for(long long p = 1; p <= P && iter < L/*&& tmpFSum < fSum*/; ++p)
            for(int k = 1; k <= K && iter < L /*&& tmpFSum < fSum*/; ++k){
                result += p*freq[iter++];
            }
        printf("Case #%d: %lld\n", tc, result);
    }
    return 0;
}
