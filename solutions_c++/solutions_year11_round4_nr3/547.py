#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int table[1000];
int Q[1000];
int Q_num;
int low, high, my_count;


void init(){
    Q_num = 0;
    int i, j;
    for(i = 2; i < 1001; ++i){
        for(j = 0; j < Q_num; ++j){
            if(i%Q[j] == 0){
                break;
            }
        }
        if(j == Q_num){
            Q[Q_num++] = i;
        }
    }
    for(i = 0; i < Q_num; ++i){
        //printf("%d ", Q[i]);
    }
}

void XD(int num){
    int i = 0;
    int count;
    int flag = 0;
    for(i = 0; i < Q_num;++i){
        count = 0;
        while(num%Q[i] == 0){
            num/=Q[i];
            count++;
            //printf("%d %d\n", i, num);
        }
        if(count > table[i]){
            table[i] = count;
            flag = 1;
        }
    }
    //puts("");
    if(flag == 1){
        high++;
    }
}

int main(){

    int test_case, n , i, j;
    init();
    freopen("cin.txt", "r", stdin);
    freopen("cout.txt", "w", stdout);

    scanf("%d", &test_case);


    for(i = 0; i < test_case; ++i){
        scanf("%d", &n);
        low= 0;
        high = 1;
        memset(table, 0, 1000*sizeof(int));

        for(j = 2; j <= n; ++j){
            XD(j);
        }

        for(j = 0; j < Q_num; ++j){
            if(table[j] > 0){
                low++;
            }
        }
        //printf("%d %d\n", high, low);
        if(n == 1){
            printf("Case #%d: 0\n", i+1);
        }
        else{
            printf("Case #%d: %d\n", i+1, high-low);
        }

    }

    return 0;
}
