#include<cstdio>
#include<iostream>
using namespace std;
main()
{
      freopen("codejam13_0_1_in.txt", "r", stdin);
      freopen("codejam13_0_1_out.txt", "w", stdout);
      int t;
      scanf("%d", &t);
      for(int tt=1; tt<=t; tt++)
      {
              printf("Case #%d: ", tt);
              char a[5][5];
              for(int i=0; i<4; i++)
                      scanf("%s", a[i]);
              
              bool flagx=false;
              for(int i=0; i<4; i++)
              {
                     bool temp=true;
                     for(int j=0; j<4; j++)
                             if(a[i][j]!='X' && a[i][j]!='T')
                             {
                                      temp=false;
                                      break;
                             }
                     if(temp==true)
                     {
                            flagx=true;
                            break;
                     }
              }
              if(flagx==true)
              {
                             printf("X won\n");
                             continue;
              }              
              for(int i=0; i<4; i++)
              {
                     bool temp=true;
                     for(int j=0; j<4; j++)
                             if(a[j][i]!='X' && a[j][i]!='T')
                             {
                                      temp=false;
                                      break;
                             }
                     if(temp==true)
                     {
                            flagx=true;
                            break;
                     }
              }
              if(flagx==true)
              {
                             printf("X won\n");
                             continue;
              }
              for(int i=0; i<4; i++)
              {
                     if(a[i][i]!='X' && a[i][i]!='T')
                     {
                              flagx=false;
                              break;
                     }
                     if(i==3)
                             flagx=true;
              }
              if(flagx==true)
              {
                             printf("X won\n");
                             continue;
              }
              
              for(int i=0; i<4; i++)
              {
                     if(a[i][3-i]!='X' && a[i][3-i]!='T')
                     {
                              flagx=false;
                              break;
                     }
                     if(i==3)
                             flagx=true;
              }
              if(flagx==true)
              {
                             printf("X won\n");
                             continue;
              }
              
              bool flago=false;
              for(int i=0; i<4; i++)
              {
                     bool temp=true;
                     for(int j=0; j<4; j++)
                             if(a[i][j]!='O' && a[i][j]!='T')
                             {
                                      temp=false;
                                      break;
                             }
                     if(temp==true)
                     {
                            flago=true;
                            break;
                     }
              }
              if(flago==true)
              {
                             printf("O won\n");
                             continue;
              }              
              for(int i=0; i<4; i++)
              {
                     bool temp=true;
                     for(int j=0; j<4; j++)
                             if(a[j][i]!='O' && a[j][i]!='T')
                             {
                                      temp=false;
                                      break;
                             }
                     if(temp==true)
                     {
                            flago=true;
                            break;
                     }
              }
              if(flago==true)
              {
                             printf("O won\n");
                             continue;
              }
              for(int i=0; i<4; i++)
              {
                     if(a[i][i]!='O' && a[i][i]!='T')
                     {
                              flago=false;
                              break;
                     }
                     if(i==3)
                             flago=true;
              }
              if(flago==true)
              {
                             printf("O won\n");
                             continue;
              }
              for(int i=0; i<4; i++)
              {
                     if(a[i][3-i]!='O' && a[i][3-i]!='T')
                     {
                              flago=false;
                              break;
                     }
                     if(i==3)
                             flago=true;
              }
              if(flago==true)
              {
                             printf("O won\n");
                             continue;
              }
              bool flagcont=false;
              for(int i=0; i<4; i++)
              {
                      for(int j=0; j<4; j++)
                              if(a[i][j]=='.')
                              {
                                              flagcont=true;
                                              break;                                
                              }
                              if(flagcont==true)
                                                break;
              }
              if(flagcont==true)
              {
                                printf("Game has not completed\n");
                                continue;
              }
              printf("Draw\n");
      }
}
