#include<iostream>
using namespace std;

main()
{
    int t, k;
    char game[4][4];
    cin>>t;
    for(k=1;k<=t;k++)
    {
              int incomplete=0,flag=0;

              for(int i=0;i<4;i++)
              for(int j=0;j<4;j++)
              {cin>>game[i][j];
              if(game[i][j]=='.'&&incomplete==0)
              incomplete=1;
              }

              for(int i=0;i<4;i++)
              if(game[i][0]!='O' && game[i][1]!='O'&& game[i][2]!='O' && game[i][3]!='O' && game[i][0]!='.' && game[i][1]!='.'&& game[i][2]!='.' && game[i][3]!='.')
              {
                     cout<<"Case #"<<k<<": X won"<<"\n";

                     flag=1;
                     break;
              }
              if(flag==1)
              continue;

              for(int i=0;i<4;i++)
              if(game[0][i]!='O' && game[1][i]!='O'&& game[2][i]!='O' && game[3][i]!='O' && game[0][i]!='.' && game[1][i]!='.'&& game[2][i]!='.' && game[3][i]!='.')
              {
                     cout<<"Case #"<<k<<": X won"<<"\n";

                     flag=1;
                     break;
              }
              if(flag==1)
              continue;

              for(int i=0;i<4;i++)
              if(game[i][0]!='X' && game[i][1]!='X'&& game[i][2]!='X' && game[i][3]!='X' && game[i][0]!='.' && game[i][1]!='.'&& game[i][2]!='.' && game[i][3]!='.')
              {
                     cout<<"Case #"<<k<<": O won"<<"\n";

                     flag=1;
                     break;
              }
              if(flag==1)
              continue;

              for(int i=0;i<4;i++)
              if(game[0][i]!='X' && game[1][i]!='X'&& game[2][i]!='X' && game[3][i]!='X'  && game[0][i]!='.' && game[1][i]!='.'&& game[2][i]!='.' && game[3][i]!='.')
              {
                     cout<<"Case #"<<k<<": O won"<<"\n";

                     flag=1;
                     break;
              }
              if(flag==1)
              continue;

              if(game[0][0]!='O' && game[1][1]!='O'&& game[2][2]!='O' && game[3][3]!='O' && game[0][0]!='.' && game[1][1]!='.'&& game[2][2]!='.' && game[3][3]!='.')
              {
                     cout<<"Case #"<<k<<": X won"<<"\n";
                     continue;
              }

              if(game[3][0]!='O' && game[2][1]!='O'&& game[1][2]!='O' && game[0][3]!='O' && game[3][0]!='.' && game[2][1]!='.'&& game[1][2]!='.' && game[0][3]!='.')
              {
                     cout<<"Case #"<<k<<": X won"<<"\n";
                     continue;
              }

              if(game[0][0]!='X' && game[1][1]!='X'&& game[2][2]!='X' && game[3][3]!='X'  && game[0][0]!='.' && game[1][1]!='.'&& game[2][2]!='.' && game[3][3]!='.')
              {
                     cout<<"Case #"<<k<<": O won"<<"\n";
                     continue;
              }

              if(game[0][3]!='X' && game[1][2]!='X'&& game[2][1]!='X' && game[3][0]!='X'  && game[0][3]!='.' && game[1][2]!='.'&& game[2][1]!='.' && game[3][0]!='.')
              {
                     cout<<"Case #"<<k<<": O won"<<"\n";
                     continue;
              }


              if(incomplete==0)
              cout<<"Case #"<<k<<": Draw"<<"\n";

              else
              cout<<"Case #"<<k<<": Game has not completed"<<"\n";
    }
}
