#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
main()
{
      int t,x,y,flag,win;
      char mat[4][7];
      scanf("%d",&t);
      for(int i=0;i<t;i++)
      {
              x=-1;y=-1;flag=0;
              for(int j=0;j<4;j++)
              scanf("%s",&mat[j]);
              for(int j=0;j<4;j++) //row
              {
                      win=0;
                      for(int k=0;k<4;k++)
                      if(mat[j][k]==mat[j][0] || mat[j][k]=='T')
                      win++;
                      if(win==4 && mat[j][0]!='.')
                      {flag=1;x=j;y=0;break;}
              }
              if(flag==1)
              {printf("Case #%d: %c won\n",i+1,mat[x][y]);continue;}
              for(int j=0;j<4;j++) //coloumn
              {
                      win=0;
                      for(int k=0;k<4;k++)
                      if(mat[k][j]==mat[0][j] || mat[k][j]=='T')
                      win++;
                      if(win==4 && mat[0][j]!='.')
                      {flag=1;x=0;y=j;break;}
              }
              if(flag==1)
              {printf("Case #%d: %c won\n",i+1,mat[x][y]);continue;}
              win=0;
              for(int j=0;j<4;j++)//d1
              {
                      if(mat[j][j]==mat[0][0] || mat[j][j]=='T')
                      win++;
              }
              if(win==4 &&  mat[0][0]!='.')
              {printf("Case #%d: %c won\n",i+1,mat[0][0]);continue;}
              win=0;
              for(int j=0;j<4;j++)//d2
              {
                      if(mat[j][3-j]==mat[0][3] || mat[j][3-j]=='T')
                      win++;
              }
              if(win==4 && mat[0][3]!='.')
              {printf("Case #%d: %c won\n",i+1,mat[0][3]);continue;}
              flag=0;
              for(int j=0;j<4;j++)
              for(int k=0;k<4;k++)
              if(mat[j][k]=='.')
              {flag=1;break;}
              if(flag==1)
              printf("Case #%d: Game has not completed\n",i+1);
              else
              printf("Case #%d: Draw\n",i+1);

}




          system("pause");
      }
