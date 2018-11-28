#include <cstdio>
#include <algorithm>

using namespace std;

long long T1[1000];
long long T2[1000];
int T, N;

int main() {

    scanf("%d", &T);
    for (int t=0; t<T; t++) {
        scanf("%d", &N);
        for (int i=0; i<N; i++) scanf("%lld", &T1[i]);
        for (int i=0; i<N; i++) scanf("%lld", &T2[i]);
        sort(T1, T1+N);
        sort(T2, T2+N);
        long long result=0;
        for (int i=0; i<N; i++) result+=T1[i]*T2[N-1-i];
        printf("Case #%d: %lld\n", t+1, result);        
    }
    
    return 0;
}
