#include <cstdio>
#include <cstdlib>

using namespace std;

#define MAXN 10001

int T, N;
int A[MAXN];
int B[MAXN];

int solve(){
    int res = 0;
    
    for (int i = 0; i < N; i++){
        for (int j = i+1; j < N; j++){
            if (((A[i] < A[j]) && (B[i] > B[j])) || ((A[i] > A[j]) && (B[i] < B[j])) )
                res++;
        }
    }

    return res;
}

int main(){

    scanf("%d", &T);

    for (int i = 0; i < T; i++){

        scanf("%d", &N);

        for (int j = 0; j < N; j++){


            //for (int k = 0; k < N; k++){

                scanf("%d %d", &A[j], &B[j]);
            //}


        }
        int res;

        res = solve();
        
        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}
