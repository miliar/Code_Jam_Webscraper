int input()
{
 int t=0;
 char c;
 c=getchar_unlocked();
 while(c<'0' || c>'9')
 c=getchar_unlocked();
 while(c>='0' && c<='9')
 {
  t=(t<<3)+(t<<1)+c-'0';
  c=getchar_unlocked();
 }
 return(t);
}
#include<stdio.h>
#include<string.h>
int main()
{
    int t=input(),y=1;;
    while(t--)
    {
              char A[4][5],B[4][5];
              int i,j=0,k,f=0,flag=0;
              printf("\nCase #%d: ",y);y++;
              //puts("");
              for(i=0;i<4;i++)
              {
                              scanf("%s",A[i]);
                 //             puts(A[i]);
                              
              }
             // puts("");
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              B[i][j]=A[j][i];
                                              if(A[i][j]=='.')
                                              f++;
                              }
                              B[i][j]='\0';
               //               puts(B[i]);
              }
              int tempx=0,tempo=0,tempxx=0,tempoo=0;
              for(i=0;i<4;i++)
              {
               
               if(strcmp("XXXX",B[i])==0||strcmp("TXXX",B[i])==0||strcmp("XTXX",B[i])==0||strcmp("XXTX",B[i])==0||strcmp("XXXT",B[i])==0)
               {
                printf("X won");
                flag=1;break;
               }
               else if(strcmp("OOOO",B[i])==0||strcmp("TOOO",B[i])==0||strcmp("OTOO",B[i])==0||strcmp("OOTO",B[i])==0||strcmp("OOOT",B[i])==0)              
               {
                    printf("O won");
                    flag=1;break;
               }
               else if(strcmp("XXXX",A[i])==0||strcmp("TXXX",A[i])==0||strcmp("XTXX",A[i])==0||strcmp("XXTX",A[i])==0||strcmp("XXXT",A[i])==0)
               {
                printf("X won");
                flag=1;break;
               }
               else if(strcmp("OOOO",A[i])==0||strcmp("TOOO",A[i])==0||strcmp("OTOO",A[i])==0||strcmp("OOTO",A[i])==0||strcmp("OOOT",A[i])==0)              
               {
                    printf("O won");
                    flag=1;break;
               }
               else
               {
                   if(A[i][i]=='X'||A[i][i]=='T')
                   tempx++;
                   if(A[i][i]=='O'||A[i][i]=='T')
                   tempo++;
                   
                   if(A[i][3-i]=='X'||A[i][3-i]=='T')
                   tempxx++;
                   if(A[i][3-i]=='O'||A[i][3-i]=='T')
                   tempoo++;

               }              
              }
              if(flag==1)
              continue;
              else if(tempx==4||tempxx==4)
              {
              
                printf("X won");
                continue;
               
              }
              else if(tempo==4||tempoo==4)
              {
              
                printf("O won");
                continue;
               
              }
              
              else if(f>0)
              {
                     printf("Game has not completed");
                     continue;
              }
              else
              printf("Draw");
    }
}
