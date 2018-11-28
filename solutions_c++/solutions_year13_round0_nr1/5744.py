#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<fstream.h>
using namespace std;
main()
{
      int t,i,j,row,col,countdot,cnt,k;
      char line[5][5],partpt,winner;
      cin>>t;
      ofstream f;
      f.open("c:\\output.txt");
      for(i=0;i<t;i++)
      {
              for(j=0;j<4;j++)
              {
                      cin>>line[j];
                     // fflush(stdin);
                      }
              
              countdot=0;
              winner='N';
              for(k=0;k<4;k++)
              {
                              for(j=0;j<4;j++)
                              {
                                              partpt=line[k][j];
                                              if(partpt!='.')
                                              {   
                                                                  cnt=1;
                                                                  row=k;
                                                                  col=j;
                                                          if(row == 0)
                                                          {
                                                                  row++;
                                                                  while((line[row][col]==partpt || line[row][col]=='T') && row<4)
                                                                  {
                                                                                                row++;
                                                                                                cnt++;
                                                                                                }
                                                                  if(cnt == 4)
                                                                  {
                                                                         winner=partpt;
                                                                         break;
                                                                         }
                                                          }
                                                                  cnt=1;
                                                                  row=k;
                                                          if(col == 0)
                                                          {
                                                                  col++;
                                                                  while((line[row][col]==partpt || line[row][col]=='T') && col<4)
                                                                  {
                                                                                                cnt++;
                                                                                                col++;
                                                                                                }
                                                                  if(cnt == 4)
                                                                  {
                                                                         winner=partpt;
                                                                         break;
                                                                         }
                                                          }
                                                                  cnt=1;
                                                                  row=k;
                                                                  col=j;
                                                          if(col == 0 && row == 0)
                                                          {
                                                                  row++;
                                                                  col++;
                                                                  while((line[row][col]==partpt || line[row][col]=='T') && col<4 && row<4)
                                                                  {
                                                                                               cnt++;
                                                                                               col++;
                                                                                               row++;
                                                                                               }
                                                                  if(cnt == 4)
                                                                  {
                                                                         winner=partpt;
                                                                         break;
                                                                         }
                                                          }
                                                                  cnt=1;
                                                                  row=k;
                                                                  col=j;
                                                          if(col == 3 && row == 0)
                                                          {
                                                                  row++;
                                                                  col--;
                                                                  while((line[row][col]==partpt || line[row][col]=='T') && row<4 && col>=0 )
                                                                  {
                                                                                               cnt++;
                                                                                               col--;
                                                                                               row++;
                                                                                               }
                                                                  if(cnt == 4)
                                                                  {
                                                                         winner=partpt;
                                                                         break;
                                                                         }
                                                          }
                                              }
                                              else
                                               countdot++;
                              }
                              if(winner!= 'N')
                              break;                
              }
              if(winner != 'N')
              {
                        f <<"Case #"<<i+1<<": "<<winner<<" won\n";
                  //      ans[i][0]=winner;
                  //      strcat(ans[i]," won");
                        }
              else if(winner == 'N' && countdot > 0)
              {
                        f <<"Case #"<<i+1<<": "<<"Game has not completed\n";     
                  //      strcpy(ans[i],"Game has not completed");
                        }
              else
              {
                        f <<"Case #"<<i+1<<": "<<"Draw\n";     
                  //      strcpy(ans[i],"Draw");
                        }
              //cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
      }
      
/*for(i=0;i<t;i++)
{
               f <<"Case #"<<i+1<<": "<<ans[i]<<"\n";
                  
                }*/
                f.close();
getch();
}
