#include<stdio.h>
int b[4][4];
int status()
{
     int Left=0,set,i,j,r,q;
     for(int i=0;i<4;i++)
     {
             for(int j=0;j<4;j++)
             {
                     if(b[i][j]==46)
                                    Left=1;
             }
     }
     for(i=0;i<4;i++)
     {
                     for(int r=0;r<4;r++)
                     {
                             set=b[i][r];
                             if(set==84||set==46)
                                        continue;
                             else 
                                  break;
                     }
                     if(set==84||set==46)
                                         continue;
                     
                     for(j=0;j<4;j++)
                     {
                             if(b[i][j]==46)
                                            Left=1;
                             if(b[i][j]==set||b[i][j]==84)
                                                  continue;
                             else
                                 break;                     
                     }
                     if(j==4&&b[i][0]!=84)
                                          return b[i][0]; 
                     else if(j==4)
                          return b[i][1];             
     }
     
     for(j=0;j<4;j++)
     {
                     for(int r=0;r<4;r++)
                     {
                             set=b[r][j];
                             if(set==84||set==46)
                                        continue;
                             else 
                                  break;
                     }
                     if(set==84||set==46)
                                         continue;
                     
                     for(i=0;i<4;i++)
                     {
                             if(b[i][j]==46)
                                            Left=1;
                             if(b[i][j]==set||b[i][j]==84)
                                                  continue;
                             else
                                 break;                     
                     }
                     if(i==4&&b[0][j]!=84)
                                          return b[0][j]; 
                     else if(i==4)
                          return b[0][j];    
                       
     }
     //Diagonal 1
      for(r=0,q=0;r<4&&q<4;r++,q++)
      {
                                  set=b[r][q];
                                  if(set==84||set==46)
                                                      continue;
                                  else 
                                       break;
      }
      if(set==84||set==46)
                          ;
      else
      {
          for(i=0,j=0;i<4&&j<4;i++,j++)
          {                           
                                      if(b[i][j]==set||b[i][j]==84)
                                                                  continue;
                                      else 
                                           break;
          }
          if(i==4&&j==4&&b[0][0]!=84)
                                return b[0][0];
          else if(i==4&&j==4)
                             return b[1][1];
      }
      
     //Diagonal 2
     for(r=0,q=3;r<4&&q>-1;r++,q--)
     {
                                  set=b[r][q];
                                  if(set==84||set==46)
                                                      continue;
                                  else 
                                       break;
      }
      if(set==84||set==46)
                          ;
      else
      {
          for(i=0,j=3;i<4&&j>-1;i++,j--)
          {                           
                                      if(b[i][j]==set||b[i][j]==84)
                                                                  continue;
                                      else 
                                           break;
          }
          if(i==4&&j==-1&&b[0][3]!=84)
                                return b[0][3];
          else if(i==4&&j==-1)
                             return b[1][2];
      }
     
     if(Left==1)
                return 0;
     else
         return 1;
}
int main()
{
    freopen ("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,stat,q=0;
    char a[5];
    scanf("%d",&t);
    getchar();
    while(t--)
    {
              q++;
              for(i=0;i<4;i++)
              {
                      gets(a);
                      for(j=0;j<4;j++)
                                      b[i][j]=a[j];
              }          
              stat=status();
              
              if(stat==1)
                         printf("Case #%d: Draw\n",q);
              else if(stat==0)
                              printf("Case #%d: Game has not completed\n",q);
              else if(stat==88)
                               printf("Case #%d: X won\n",q);
              else if(stat==79)
                               printf("Case #%d: O won\n",q);
              getchar();  
    }
    return 0;
}
