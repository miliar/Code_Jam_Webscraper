#include<stdio.h>
#include<stdlib.h>


int main(int argc, char *argv[]){

    int testcase;
    int num;

    int temp;

    int o_count;
    int b_count;

    int b, o;

    int last_b;
    int last_o;

    char color[10];
    int z, i;


    freopen("test.in", "r", stdin);
    freopen("test.out","w", stdout );

    scanf("%d", &testcase) ;
    for(z = 0; z < testcase; z++){
        scanf("%d", &num);
        o_count = 0;
        b_count = 0;

        last_b = 1;
        last_o = 1;
        for(i = 0; i < num; ++i){
            scanf("%s", color);

            scanf("%d", &temp);
            if(color[0] == 'O'){
                if(last_o - temp < 0){
                    o = temp - last_o;
                }
                else{
                    o = last_o - temp;
                }

                last_o = temp;

                if(o_count + o >= b_count){
                    o_count += (o + 1);
                }
                else{
                    o_count = b_count + 1;
                }
            }
            else{
                if(last_b - temp < 0){
                    b = temp - last_b;
                }
                else{
                    b = last_b - temp;
                }

                last_b = temp;
                //printf("b %d %d %d\n", b_count, b , o_count);
                if(b_count + b >= o_count){
                    b_count += (b + 1);
                }
                else{
                    b_count = o_count+1;
                }
            }
            //printf("%d %d\n", o_count, b_count);
        }

        printf("Case #%d: ", z+1);

        if(b_count > o_count){
            printf("%d\n", b_count);
        }
        else{
            printf("%d\n", o_count);
        }

    }
	return 0;
}
