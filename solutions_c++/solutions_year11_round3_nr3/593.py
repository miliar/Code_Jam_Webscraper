#include<stdio.h>
#include<stdlib.h>


int gcd(int a, int b){
    if(b == 0){
        return a;
    }
    else{
        return gcd(b ,a%b);
    }
}

int compare(const void* a, const void *b){
    int c = *(int*)a;
    int d = *(int*)b;

    if(c > d){
        return 1;
    }
    else if(c < d){
        return -1;
    }
    else{
        return 0;
    }
}

int main(int argc, char *argv[]){

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int testcase, i, j, k;
    int num ,low, high;
    int numbers[1000];
    int ans;
    int temp;
    int ok;

    scanf("%d", &testcase);

    for(i = 0; i < testcase; ++i){
        scanf("%d %d %d", &num, &low, &high);
        for(j = 0; j < num; ++j){
            scanf("%d", &numbers[j]);
        }
        qsort(numbers, num, sizeof(int),compare);

        ans = numbers[0];

        for(j = low; j <= high; ++j){
            ok = 1;
            for(k = 0; k < num; ++k){
                if(numbers[k] > j){
                    if(numbers[k]%j != 0){
                        ok = 0;
                        break;
                    }
                }
                else{
                    if(j%numbers[k] != 0){
                        ok = 0;
                        break;
                    }
                }
            }
            if(ok){
                break;
            }
        }


        printf("Case #%d: ", i+1);
        if(!ok){
            printf("NO\n");
        }
        else{

            printf("%d\n", j);
        }


    }

	return 0;
}
