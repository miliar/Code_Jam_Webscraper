#include <cstdio>
#include <cstdlib>
#include <ctime>

int hei[2010];
int ob[2010];

int main(){

    int t;
    scanf("%d" ,&t);

    srand(time(NULL));
    for(int T = 1; T <= t; T++){

        int n;
        scanf("%d" ,&n);

        for(int i = 1; i <= n; i++) hei[i] = 0;
        for(int i = 1; i < n; i++) scanf("%d" ,&ob[i]);

        bool flag = true;
        for(int i = 1; i < n && flag; i++){
            for(int j = i + 1; j < ob[i] && flag; j++){
                if(ob[j] > ob[i]) flag = false;
            }
        }
        if(!flag){
            printf("Case #%d: Impossible\n" ,T);
            continue;
        }

        int count = n * 100;
        while(count != 0){
            for(int i = 1; i < n; i++){
                for(int j = i + 1; j <= n; j++){
                    long long lv = (long long)(hei[j] - hei[i]) * (ob[i] - i);
                    long long rv = (long long)(hei[ob[i]] - hei[i]) * (j - i);
                    if(lv > rv || (j < ob[i] && lv >= rv)){
                        if(hei[ob[i]] > hei[j] && (rand() % 32 == 0)){
                            hei[i] += rand() % 5 + 1;
                        }
                        else hei[ob[i]] += rand() % 5 + 1;
                        goto end;
                    }
                }
            }
            break;
            end:
            count--;
        }

        /*if(count == 0){
            printf("Case #%d: Impossible\n" ,T);
            continue;
        }*/

        printf("Case #%d:" ,T);
        for(int i = 1; i <= n; i++) printf(" %d" ,hei[i]);
        putchar('\n');

    }

}
