#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int t,i,j,k;
    char a[5][5];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
                     
                     scanf("%s",a[0]);
                     scanf("%s",a[1]);
                     scanf("%s",a[2]);
                     scanf("%s",a[3]);
                     for(j=0;j<4;j++)
                     {
                                     for(k=0;k<4;k++)
                                     {
                                              if(a[j][k]!='X'&& a[j][k]!='T')
                                              break;
                                     }
                                     if(k==4){
                                     printf("Case #%d: X won\n",i);break;}
                     }
                     if(j!=4)
                     continue;
                     
                     for(j=0;j<4;j++)
                     {
                                     for(k=0;k<4;k++)
                                     {
                                              if(a[k][j]!='X'&& a[k][j]!='T')
                                              break;
                                     }
                                     if(k==4){
                                     printf("Case #%d: X won\n",i);break;}
                     }
                     if(j!=4)
                     continue;
                     
                     if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
                     {        printf("Case #%d: X won\n",i); continue;
                     }
                       if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
                     {        printf("Case #%d: X won\n",i); continue;
                     }
                   
                    
                    
                     
                     
                     for(j=0;j<4;j++)
                     {
                                     for(k=0;k<4;k++)
                                     {
                                              if(a[j][k]!='O'&&a[j][k]!='T')
                                              break;
                                     }
                                     if(k==4){
                                     printf("Case #%d: O won\n",i);break;}
                     }
                     if(j!=4)
                     continue;
                     
                     for(j=0;j<4;j++)
                     {
                                     for(k=0;k<4;k++)
                                     {
                                              if(a[k][j]!='O'&&a[k][j]!='T')
                                              break;
                                     }
                                     if(k==4){
                                     printf("Case #%d: O won\n",i);break;}
                     }
                     if(j!=4)
                     continue;
                     
                     if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
                     {        printf("Case #%d: O won\n",i); continue;
                     }
                       if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
                     {        printf("Case #%d: O won\n",i); continue;
                     }
                         
                    for(j=0;j<4;j++)
                    {
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[j][k]=='.')
                                                    break;
                                    }
                                    if(k!=4){
                                    printf("Case #%d: Game has not completed\n",i);break;
                                    }
                    }
                    if(j!=4)
                    continue;
                    
                    printf("Case #%d: Draw\n",i);
    }
        return 0;
}
                    
                    
                         
                                                    
                                                     
