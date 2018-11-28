#include<stdio.h>
#define ABS(x) (((x)>0)?(x):-(x))

int main(){
    int T,N,cas=0,O=0,B=0,Op=1,Bp=1,pos,temp;

    char bot;
    scanf("%d",&T);
    while (cas++ <T) {
        O=B=0;
        Op=Bp=1;
        scanf("%d ",&N);
//        printf("N:%d\n",N);
        for(int i =0;i < N;i++){
            scanf("%c %d ",&bot,&pos);
//            printf("move: %c %d\n",bot,pos);
            if(bot == 'O') {
                temp = pos-Op;
//                printf("%d",temp);
//                printf("\nO:%d B:%d \n",O,B);
                O += ABS(temp);   
//                printf("\nO:%d B:%d \n",O,B);
                O = ((O>B)?(O+1):(B+1));
//                printf("\nO:%d B:%d \n",O,B);
                Op = pos;
            }
            else {
                temp = pos - Bp;
//                printf("%d,%d,%d",temp,pos,Bp);
//                printf("\nO:%d B:%d \n",O,B);
                B += ABS(temp);
//                printf("\nO:%d B:%d \n",O,B);
                B = ((B>O)?B+1:O+1);
//                printf("\nO:%d B:%d \n",O,B);
                Bp = pos;
            }
        }
        temp = ((B>O)?B:O);
        printf("Case #%d: %d\n",cas,temp);
    }
    return 0;
}
