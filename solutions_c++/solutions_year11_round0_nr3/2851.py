#include<stdio.h>
#include<stdlib.h>
int candy[2000];
int num, max;

int DtoB(int num, char str[]){
    int i = 0;
    while(num){
        str[i++] = num%2;
        num/=2;
    }
    return i;
}

int PatrickAdd(int a, int b){

    char binary_a[1000], binary_b[1000], binary_str[1000];
    int binary_a_length, binary_b_length, binary_str_length;
    int i, multiplier, total;

    binary_a_length = DtoB(a, binary_a);
    binary_b_length = DtoB(b, binary_b);

    if(binary_a_length > binary_b_length){
        for(i = 0; i < binary_b_length; ++i){
            binary_str[i] = (binary_a[i] + binary_b[i])%2;
        }
        for(; i < binary_a_length; ++i){
            binary_str[i] = binary_a[i];
        }
        binary_str_length = binary_a_length;
    }
    else{
        for(i = 0; i < binary_a_length; ++i){
            binary_str[i] = (binary_a[i] + binary_b[i])%2;
        }
        for(; i < binary_b_length; ++i){
            binary_str[i] = binary_b[i];
        }
        binary_str_length = binary_b_length;
    }

    for(i = 0, multiplier = 1, total = 0; i < binary_str_length; ++i, multiplier*=2){
        if(binary_str[i] == 1){
            total += multiplier;
        }
    }
    return total;
}


void doSplit(int a, int b, int temp1, int temp2, int count){
    if(count >= num){
        if(temp1 == 0 || temp2 == 0){
            return;
        }
        if(a == b){
            if(temp1 > max){
                max = temp1;
            }
            if(temp2 > max){
                max = temp2;
            }
            //printf("%d %d %d %d\n", a,b,temp1,temp2);
        }
        return;
    }
    else{
        // select for a
        doSplit(PatrickAdd(a, candy[count]), b, candy[count] + temp1, temp2, count + 1);

        // select for b
        doSplit(a, PatrickAdd(b, candy[count]), temp1, candy[count] + temp2, count + 1);
    }

}

int main(int argc, char *argv[]){
    //printf("%d\n", PatrickAdd(544384, 607839));
    //return 0;
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int testcase;

    int i, j, k;

    int a, b;

    int temp1, temp2;

    scanf("%d", &testcase);

    for(i = 0; i < testcase; ++i){
        scanf("%d", &num);
        for(j = 0; j < num; ++j){
            scanf("%d", &candy[j]);
        }


        max = -1;
        doSplit(0, 0, 0, 0, 0);

/*
        for(j = 1; j < num; ++j){
            a = 0;
            b = 0;
            temp1 = 0;
            temp2 = 0;
            for(k = 0; k < j; ++k){
                a = PatrickAdd(a, candy[k]);
                temp1 += candy[k];
            }
            for(;k < num; ++k){
                b = PatrickAdd(b, candy[k]);
                temp2 += candy[k];
            }
            //printf("%d %d %d %d\n", a, b, temp1, temp2);
            if(a == b){
                if(temp1 > max){
                    max = temp1;
                }
                if(temp2 > max){
                    max = temp2;
                }
            }
        }
*/
        if(max == -1){
            printf("Case #%d: NO\n", i+1);
        }
        else{
            printf("Case #%d: %d\n", i+1, max);
        }
    }

	return 0;
}
