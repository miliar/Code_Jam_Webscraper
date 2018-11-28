

#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int freq[1000], N, K, lim, wl[100], L, sum;
char W[100][2000], expr[10000];

void go(int lv){
        if (lv == lim){
                int tmp = 0;
                int prod = 1;
                for (int i = 0 ; i < L; ++i)
                        if (expr[i] == '+')
                                tmp = (tmp + prod)%10009, prod=1;
                        else prod = (prod * (freq[expr[i]]%10009))%10009;
                tmp = (tmp + (prod%10009))%10009;
                sum = (sum + tmp) % 10009;
        }else
                for (int i = 0 ; i < N; ++i){
                        for (int j = 0 ; j < wl[i]; ++j)
                                freq[W[i][j]]++;
                        go(lv+1);
                        for (int j = 0 ; j < wl[i]; ++j)
                                freq[W[i][j]]--;
                }
}

int main(){
        int T, ca=0;
        scanf("%d", &T);
        while (T--){
                scanf("%s%d", expr, &K);
                memset(freq, 0, sizeof(freq));
                L = strlen(expr);
                scanf("%d", &N);
                for (int i = 0 ; i < N; ++i)
                        scanf("%s", W[i]), wl[i] = strlen(W[i]);
                printf("Case #%d:", ++ca);
                for (int i =  1; i <= K; ++i){
                        lim = i;
                        sum = 0;
                        go(0);
                        printf(" %d", sum);
                }
                puts("");
        }
        return 0;
}
