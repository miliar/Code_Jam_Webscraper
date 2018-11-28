#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int valid[105];
char stack[105] ;
char s[105];
char comb[105][10],opp[105][10];
int main (){
    int T,C,D,n,i,j,flag,next,k,pos,ca = 0,pre;
    int top;
    char other;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&C);
        for(i=0;i<C;i++){
            scanf("%s",comb[i]);
        }
        scanf("%d",&D);
        for(i=0;i<D;i++){
            scanf("%s",opp[i]);
        }
        scanf("%d%s",&n,s);
        for(i=0;i<n;i++)valid[i] = 1;
        top = 0;
        for(i=0;i<n;i++){
            stack[top] = s[i];
            top++;
           // printf("top %d\n",top);
            if(top == 1)continue;
            for(j=0;j<C;j++){
                if(stack[top-1] == comb[j][1] && stack[top-2] == comb[j][0]){
             //       printf("in %c\n",comb[j][2]);
                    stack[top-2] = comb[j][2];
                    top--;
                    break;
                }
                if(stack[top-1] == comb[j][0] && stack[top-2] == comb[j][1]){
            //        printf("in %c\n",comb[j][2]);
                    stack[top-2] = comb[j][2];
                    top--;
                    break;
                }
            }
            for(k=0;k<top;k++){
                for(j=0;j<D;j++){
                    if(stack[k] == opp[j][0] && stack[top-1] == opp[j][1]){
                        top = 0;
                        break;
                    }
                    if(stack[k] == opp[j][1] && stack[top-1] == opp[j][0]){
                        top = 0;
                        break;
                    }
                }
                if(top == 0)break;
            }
        }
        ca++;
        printf("Case #%d: [",ca);
        flag = 0;
        for(i=0;i<top;i++){
            if(flag == 1)printf(", ");
            printf("%c",stack[i]);
            flag = 1;
        }
        printf("]\n");
    }
    return 0;
}
/*
6
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW


0 <= C <= 36.
0 <= D <= 28.
1 <= N <= 100.
*/

