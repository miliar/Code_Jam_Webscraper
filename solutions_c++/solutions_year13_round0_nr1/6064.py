#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int main()
{
    int c;
    cin>>c;
    for(int t=1;t<=c;t++)
    {
              char a[4][4];
              int gno=0,flag=0;
              
              for(int i=0;i<4;i++)
              for(int j=0;j<4;j++)
              {cin>>a[i][j];
              if(a[i][j]=='.'&& gno==0)
              gno=1;
              }
              
              // X row wise
              for(int i=0;i<4;i++)
              if(a[i][0]!='O' && a[i][1]!='O'&& a[i][2]!='O' && a[i][3]!='O' && a[i][0]!='.' && a[i][1]!='.'&& a[i][2]!='.' && a[i][3]!='.')
              {
                     cout<<"Case #"<<t<<": X won"<<endl;
                     
                     flag=1; 
                     break;           
              }
              if(flag==1)
              continue;
              
              // X column wise
              for(int i=0;i<4;i++)
              if(a[0][i]!='O' && a[1][i]!='O'&& a[2][i]!='O' && a[3][i]!='O' && a[0][i]!='.' && a[1][i]!='.'&& a[2][i]!='.' && a[3][i]!='.')
              {
                     cout<<"Case #"<<t<<": X won"<<endl;
                     
                     flag=1;
                     break;            
              }
              if(flag==1)
              continue;
              
              
              // O row wise
              for(int i=0;i<4;i++)
              if(a[i][0]!='X' && a[i][1]!='X'&& a[i][2]!='X' && a[i][3]!='X' && a[i][0]!='.' && a[i][1]!='.'&& a[i][2]!='.' && a[i][3]!='.')
              {
                     cout<<"Case #"<<t<<": O won"<<endl;
                    
                     flag=1;
                     break;           
              }
              if(flag==1)
              continue;
              
              // O column wise
              for(int i=0;i<4;i++)
              if(a[0][i]!='X' && a[1][i]!='X'&& a[2][i]!='X' && a[3][i]!='X'  && a[0][i]!='.' && a[1][i]!='.'&& a[2][i]!='.' && a[3][i]!='.')
              {
                     cout<<"Case #"<<t<<": O won"<<endl;
                     
                     flag=1; 
                     break;           
              }
              if(flag==1)
              continue;
              
              //X wins diagonally
              if(a[0][0]!='O' && a[1][1]!='O'&& a[2][2]!='O' && a[3][3]!='O' && a[0][0]!='.' && a[1][1]!='.'&& a[2][2]!='.' && a[3][3]!='.')
              {
                     cout<<"Case #"<<t<<": X won"<<endl;
                     continue;            
              }
              
              //X wins diagonally
              if(a[3][0]!='O' && a[2][1]!='O'&& a[1][2]!='O' && a[0][3]!='O' && a[3][0]!='.' && a[2][1]!='.'&& a[1][2]!='.' && a[0][3]!='.')
              {
                     cout<<"Case #"<<t<<": X won"<<endl;
                     continue;            
              }
              
              //O wins diagonally
              if(a[0][0]!='X' && a[1][1]!='X'&& a[2][2]!='X' && a[3][3]!='X'  && a[0][0]!='.' && a[1][1]!='.'&& a[2][2]!='.' && a[3][3]!='.')
              {
                     cout<<"Case #"<<t<<": O won"<<endl;
                     continue;            
              }
              
              //O wins diagonally
              if(a[0][3]!='X' && a[1][2]!='X'&& a[2][1]!='X' && a[3][0]!='X'  && a[0][3]!='.' && a[1][2]!='.'&& a[2][1]!='.' && a[3][0]!='.')
              {
                     cout<<"Case #"<<t<<": O won"<<endl;
                     continue;            
              }
              
              
              if(gno==0)
              cout<<"Case #"<<t<<": Draw"<<endl;
              
              else
              cout<<"Case #"<<t<<": Game has not completed"<<endl;
              
                     
              
    }
    return 0;
}
