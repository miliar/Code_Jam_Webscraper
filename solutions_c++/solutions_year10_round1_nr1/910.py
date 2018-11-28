#include<stdio.h>
#include<stdlib.h>
char MAP[100][100];
char AFTER[100][100];
int main (){
    int tn,N,K,ca=0,i,j,top,nowR,nowB,ti,tj;
    int Rwin,Bwin;
    scanf("%d",&tn);
    while(tn--){
        scanf("%d%d%*c",&N,&K);
        for(i=0;i<N;i++)
            scanf("%s",MAP[i]);
        for(i=0;i<N;i++)
            for(j=0;j<N;j++)
                AFTER[i][j] = '.';
        for(i=N-1;i>=0;i--){
            top = N-1;
            for(j=N-1;j>=0;j--){
                if(MAP[i][j]=='R' ||MAP[i][j] == 'B'){
                    AFTER[top][N-i-1] = MAP[i][j];
                    top--;
                }
            }
        }
   /* for(i=0;i<N;i++){
        for(j=0;j<N;j++)
            printf("%c",AFTER[i][j]);
    printf("\n");
  
}*/ 
        Rwin = 0;Bwin = 0;
        for(i=N-1;i>=0;i--){
            nowR = 0;nowB = 0;
            for(j=0;j<N;j++){
                if(AFTER[i][j] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[i][j] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[i][j] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
            }
        }
        for(j=N-1;j>=0;j--){
            nowR = 0;nowB = 0;
             for(i=0;i<N;i++){
                if(AFTER[i][j] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[i][j] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[i][j] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
            }
        }
        for(i=0;i<N;i++){
            ti = i;nowR = 0;nowB = 0;j = 0;
            while(ti < N && j < N){
                if(AFTER[ti][j] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[ti][j] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[ti][j] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
                ti++;j++;
            }
        }
        for(i=0;i<N;i++){
            ti = i;nowR = 0;nowB = 0;j = 0;
            while(ti >= 0 && j < N){
                if(AFTER[ti][j] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[ti][j] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[ti][j] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
                ti--;j++;
            }
        }
        
        for(j=0;j<N;j++){
            tj = j;nowR = 0;nowB = 0;i = 0;
            while(i < N && tj < N){
                if(AFTER[i][tj] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[i][tj] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[i][tj] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
                i++;tj++;
            }
        }
        for(j=0;j<N;j++){
            tj = j;nowR = 0;nowB = 0;i = N-1;
            while(i >= 0 && tj < N){
                if(AFTER[i][tj] == '.'){nowR = 0;nowB = 0;}
                if(AFTER[i][tj] == 'R'){
                    nowR++;
                    nowB  = 0;
                }
                if(AFTER[i][tj] == 'B'){
                    nowB++;
                    nowR = 0;
                }
                if(nowR == K)Rwin = 1;
                if(nowB == K)Bwin = 1;
                i--;tj++;
            }
        }
        ca++;
        printf("Case #%d: ",ca);
        if(Rwin ==0 && Bwin == 0)printf("Neither\n");
        if(Rwin ==1 && Bwin == 0)printf("Red\n");
        if(Rwin ==0 && Bwin == 1)printf("Blue\n");
        if(Rwin ==1 && Bwin == 1)printf("Both\n");
    }
    return 0;
}
