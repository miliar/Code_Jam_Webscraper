#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){

    int testcase;

    int i, j, k;
    int combine_count, opposed_count;

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    char combine[1000][5];
    char opposed[1000][5];
    char list[100000];
    int list_length;

    char out_list[100000];
    int out_list_length;

    int appeared[30];

    scanf("%d", &testcase);
    for(i = 0; i < testcase; ++i){
        scanf("%d", &combine_count);
        for(j = 0; j < combine_count; ++j){
            scanf("%s", combine[j]);
        }

        scanf("%d", &opposed_count);
        for(j = 0; j < opposed_count; ++j){
            scanf("%s", opposed[j]);
        }

        scanf("%d", &list_length);
        scanf("%s", list);

        out_list_length = 0;
        memset(appeared, 0, 30*sizeof(int));

        for(j = 0; j < list_length; ++j){
            for(k = 0; k < combine_count; ++k){
                if(j > 0 && out_list_length > 0 && ((out_list[out_list_length-1] == combine[k][0] && list[j] == combine[k][1]) || (out_list[out_list_length-1] == combine[k][1] && list[j] == combine[k][0]))){
                    appeared[list[j]-65]--;
                    appeared[out_list[out_list_length-1]-65]--;
                    out_list[out_list_length-1] = combine[k][2];
                    break;
                }
            }

            appeared[list[j]-65]++;
            if(k >= combine_count){
                out_list[out_list_length++] = list[j];

                for(k = 0; k < opposed_count; ++k){
                    if((appeared[opposed[k][0]-65] > 0 && opposed[k][1] == list[j]) || (appeared[opposed[k][1]-65] > 0 && opposed[k][0] == list[j])){
                        out_list_length = 0;
                        memset(appeared, 0, 30*sizeof(int));
                        break;
                    }
                }
            }
        }
        if(out_list_length == 0){
            printf("Case #%d: []\n", i+1);
        }
        else{
            printf("Case #%d: [%c", i+1, out_list[0]);

            for(j = 1; j < out_list_length; ++j){
                printf(", %c", out_list[j]);
            }

            printf("]\n");
        }
    }

	return 0;
}
