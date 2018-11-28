#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int numbers[1000001];

int path[1000001];
short boosters[1000001];

int main(int argc, char *argv[]){

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int testcase, i, j, k, m;
    int L, t, N, C, best_k;

    int best, temp;

    scanf("%d", &testcase);

    for(i = 0; i < testcase; ++i){
        scanf("%d %d %d %d", &L, &t, &N, &C);
        memset(boosters, 0, N * sizeof(boosters[0]));
        for(j = 0; j < C; ++j){
            scanf("%d", &numbers[j]);
        }
        best = 0;
        for(j = 0; j < N; ++j){
            path[j] = numbers[j%C];
            best += path[j];
        }

        best*=2;

        for(j = 0; j < L; ++j){
            for(k = 0; k < N; ++k){
                if(boosters[k] > 0){
                    continue;
                }
                //printf("%d %d\n", j, k);
                temp = 0;
                for(m = 0; m < N; ++m){
                    if(boosters[m] > 0 && temp > t){
                        temp += path[m];
                    }
                    else if(m == k && temp > t){
                        temp += path[m];
                    }
                    else if(boosters[m] > 0 && temp+path[m]*2 > t){
                        temp += ((t - temp) + (path[m] - (t-temp)/2));
                    }
                    else if(m == k && temp+path[m]*2 > t){
                        temp += ((t - temp) + (path[m] - (t-temp)/2));
                    }
                    else{
                        temp += path[m] * 2;
                    }
                    //printf("%d ", temp);
                }
//puts("");
                if(temp < best){
                    best = temp;
                    best_k = k;
                }
            }
            boosters[best_k] = 1;
        }
        printf("Case #%d: %d\n", i+1, best);
    }

	return 0;
}
