#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

int main(void){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n=0;
    int temp1=0;
    int temp3=0;
    char temp2='a';
    int temp4=0;
    int temp5=0;
    int pos=1;
    int count=0;
    // O=1;
    // B=2;
    scanf("%d",&n);
    int turn[n][100];
    int num[n][100];
    int round[n];
    int O[n][100];
    int B[n][100];

    for(int j=0;j<n;j++){
        round[j]=0;
    for(int i=0;i<100;i++){
        turn[j][i]=0;
        num[j][i]=0;
        O[j][i]=0;
        B[j][i]=0;

    }
}
    for(int i=0;i<n;i++){
     scanf("%d",&temp1);
     round[i]=temp1;
        for(int j=0;j<round[i];j++){
            char x;
            int y;
            scanf("%c",&x);
            scanf("%d",&y);
            scanf("%c",&temp2);
            scanf("%d",&temp3);
            if(temp2=='B'){
                 turn[i][j]=2;
                 B[i][temp4++]=temp3;
            }
            else{
                turn[i][j]=1;
                O[i][temp5++]=temp3;
            }
            num[i][j]=temp3;

        }
        temp4=0;
        temp5=0;
 /*       for(int j=0;j<temp1;j++){
        printf("turn %d : %s , num %d : %d\n",j+1,turn[0][j]==1? "orange":"-blue-",j+1,num[0][j]);
        }
*/
    }

    //หาต่ำแหน่งที่ต้องกด
    int posO=1;
    int posB=1;
    int pushO=0;
    int pushB=0;
    int checkB=0;
    int checkO=0;
    int temp6=0;
    int temp7=0;
    int ans[n];

    for(int i=0;i<n;i++){
        ans[i]=0;

        for(int j=0;j<round[i];j++){
        if(pushO==0){
        checkO=O[i][temp6++];
        pushO=1;
        }
        if(pushB==0){
        checkB=B[i][temp7++];
        pushB=1;
        }
        while(true){
            if(turn[i][j]==1){
                ans[i]++;
                if(posB<checkB) posB++;
                if(posB>checkB) posB--;
                if(posO==checkO){
                    pushO=0;
                    break;
                }
                if(posO<checkO) posO++;
                if (posO>checkO) posO--;
            }
            else if (turn[i][j]==2){
                ans[i]++;
                if(posO<checkO) posO++;
                if(posO>checkO) posO--;
                if(posB==checkB){
                    pushB=0;
                    break;
                }
                if(posB<checkB) posB++;
                if (posB>checkB) posB--;
            }
            else break;
        }
// printf("%d\n",ans[i]);
        }
     posO=1;
     posB=1;
     pushO=0;
     pushB=0;
     checkB=0;
     checkO=0;
     temp6=0;
     temp7=0;
    }
    for(int i=0;i<n;i++)
       printf("Case #%d: %d\n",i+1,ans[i]);
}
