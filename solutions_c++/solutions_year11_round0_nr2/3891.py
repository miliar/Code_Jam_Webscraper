#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>




int main(void){
    freopen("B-small-attempt6.in","r",stdin);
    freopen("B-small-attempt6.out","w",stdout);
  int n=0;
  scanf("%d",&n);
  bool checkCom[n];
  bool checkOpp[n];
  char com[n][100];
  char opp[n][100];
  int len[n];
  char string[n][100];
  int temp1=0;
  for(int i=0;i<n;i++){
    scanf("%d",&temp1);
    if(temp1==1){
         scanf("%s",com[i]);
         checkCom[i]=true;
    }
    else checkCom[i]=false;
    scanf("%d",&temp1);
     if(temp1==1){
         scanf("%s",opp[i]);
         checkOpp[i]=true;
    }
    else checkOpp[i]=false;

    scanf("%d",&len[i]);
    scanf("%s",string[i]);
    temp1=0;
  }

   int len1=0;
  int startOpp1=0;
  int startOpp2=0;
  int checkWajerOpp1=0;
  int checkWajerOpp2=0;
  int checkLast=0;
    for(int i=0;i<n;i++){
        for(int k=0;k<len[i];k++){
            len1=strlen(string[i]);
        if(checkCom[i]==false&&checkOpp[i]==false){
                break;
        }
        if(checkCom[i]==true){

            if((string[i][k]==com[i][0]&&string[i][k+1]==com[i][1])||(string[i][k]==com[i][1]&&string[i][k+1]==com[i][0])){
               if(checkWajerOpp1==1&&string[i][k]==opp[i][1]){}
               else if (checkWajerOpp2==1&&string[i][k]==opp[i][0]){}
                else {string[i][k]='%';
                string[i][k+1]=com[i][2];
                  continue;
                }
            }

        }
        if(checkOpp[i]==true){
            if(string[i][k]==opp[i][0]&&checkWajerOpp1==0){
                 checkWajerOpp1=1;
                 startOpp1=k;
            }
            if (string[i][k]==opp[i][1]&&checkWajerOpp2==0){
                 checkWajerOpp2=1;
                 startOpp2=k;
            }
            if(checkWajerOpp1==1&&checkWajerOpp2==1){
                if(startOpp1<startOpp2){
                    for(int m=0;m<=startOpp2;m++)
                        string[i][m]='%';
                } else {
                    for(int m=0;m<=startOpp1;m++)
                        string[i][m]='%';
                }
                checkWajerOpp1=0;
                checkWajerOpp2=0;
            }
        }
        }
        printf("Case #%d: [",i+1);
        for(int t=0;t<len1;t++){
            if(string[i][t]!='%'){
                printf("%c",string[i][t]);
                for(int y=t+1;y<len1;y++){
                    if(string[i][y]!='%'){
                         checkLast=1;
                         break;
                    }

               }
                 if(t==len1-1||checkLast==0) break;
                 printf(", ");
            }

            checkLast=0;
        }
        printf("]\n");
   len1=0;
   startOpp1=0;
   startOpp2=0;
   checkWajerOpp1=0;
   checkWajerOpp2=0;
   checkLast=0;
    }


}





