#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

int main(void){
       freopen("A-small-attempt5.in","r",stdin);
       freopen("A-small-attempt5.out","w",stdout);
    int n=0;
    scanf("%d",&n);
    char table[50][50];
    int check=0;
    int row=0;
    int col=0;
    int kak=0;
    int count=0;
    int checkstart=-1;


    for(int i=0;i<n;i++){
        check=0;
        row=0;
        col=0;
        kak=0;
         count=0;
         checkstart=-1;
        scanf("%d",&row);
        scanf("%d",&col);


            for(int k=0;k<row;k++){
                scanf("%s",table[k]);
            }



        for(int j=0;j<row;j++){
            for(int k=0;k<col;k++){
                if(table[j][k]=='#'&&table[j][k+1]=='#'&&table[j+1][k]=='#'&&table[j+1][k+1]=='#'){
                    table[j][k]='/';
                    table[j][k+1]='\\';
                    table[j+1][k]='\\';
                    table[j+1][k+1]='/';


            }
            else;
        }
        checkstart=-1*checkstart;
        check=0;

    }
     for(int j=0;j<row;j++){
            for(int k=0;k<col;k++){
                if(table[j][k]=='#') count++;
            }
            if(count>0){
                kak=1;
                break;
            }
            count=0;
        }

        if(kak==1){
             printf("Case #%d:\n",i+1);
             printf("Impossible\n");
             continue;
        }

        printf("Case #%d:\n",i+1);
         for(int j=0;j<row;j++){
            for(int k=0;k<col;k++){
                printf("%c",table[j][k]);
            }
            printf("\n");
         }

            }

    }




