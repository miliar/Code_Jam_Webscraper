#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define DIGILEN 12

int main(){
    int i, j, k;
    int cases;
    char input[DIGILEN], map_c[DIGILEN];
    int input_digit[DIGILEN], map_i[DIGILEN];
    long int output;
    int diff_num=1, fill_num=0;//diff==base
    
    //input T
    scanf("%d", &cases);
    
    for(i=0; i<cases; i++){
        //input a case
        scanf("%s", input);
        //be zero
        //start at 1
        input_digit[0]=1;
        map_c[0]=input[0];
        map_i[0]=1;
        for(j=1; j<DIGILEN; j++){
            input_digit[j]=-1;
            map_c[j]='!';
            map_i[j]=-1;
        }
/*        printf("in\tin_di\tmap_c\tmap_i\n");
        for(j=0; j<DIGILEN; j++){
            printf("%c\t%d\t%c\t%d\n", input[j], input_digit[j], map_c[j], map_i[j]);
        }
*/
        //count symbol
        diff_num=1;
        fill_num=0;
        for(j=1; j<strlen(input); j++){
            for(k=0; k<diff_num; k++){
                if(input[j]==map_c[k]){
                   input_digit[j]=map_i[k]; 
                   //printf("map: %c\t%d\t%c\t%d\n", input[j], input_digit[j], map_c[k], map_i[k]);
                   break;
                }
            }               
            if(k==diff_num){
                input_digit[j]=fill_num;
                map_i[diff_num]=fill_num;
                map_c[diff_num]=input[j];
                //printf("fill: %c\t%d\t%c\t%d\n", input[j], input_digit[j], map_c[k], map_i[k]);
                diff_num++;
                fill_num++;
                if(fill_num==1)
                    fill_num++;   
            }
        }
        //compute output       
        if(diff_num==1)
            diff_num=2; 
        output=0;
        for(j=0; j<strlen(input)-1; j++){
            //printf("count %d(%d): %d", j, input_digit[j], output);
            output=(output+input_digit[j])*diff_num;
            //printf("*%d =%d\n", diff_num, output);
        }
        //last
        output+=input_digit[strlen(input)-1];
        //output
        printf("Case #%d: %ld\n", i+1, output);
    }

    return 0;
}
