#include <cstdio>

using namespace std;

int solve(int N, long long K){
    int n = 2 << (N - 1);
    int k = K%n;

    if (k == n - 1){
        return 1;
    }
    else
        return 0;
    
}

int main(){
    int T, N;
    long long K;

    int res;

    scanf("%d", &T);

    for (int i = 0; i < T; i++){
        scanf("%d %lld", &N, &K);

        res = solve(N, K);
        if (res == 0)
            printf("Case #%d: OFF\n", i+1);
        else
            printf("Case #%d: ON\n", i+1);
    }
}
