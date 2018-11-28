#include <iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for (int i=1;i<=t;i++)
  {
    string x[4];int p,k;
    cin>>x[0]>>x[1]>>x[2]>>x[3];
    for (int i=0;i<4;i++)
    for (int j=0;j<4;j++)
    if (x[i][j]=='T')
    {
    x[i][j]='O';
    p=i;k=j;
    }
    
    char cc='0';
    
    for (int i=0;i<4;i++)
    if ((x[i][0]==x[i][1])&&(x[i][1]==x[i][2])&&(x[i][3]==x[i][0])&&x[i][0]=='O')
    cc=x[i][0];
    for (int i=0;i<4;i++)
    if ((x[0][i]==x[1][i])&&(x[0][i]==x[2][i])&&(x[3][i]==x[0][i])&&x[0][i]=='O')
    cc=x[0][i];
    for (int i=0;i<4;i++)
    if ((x[0][0]==x[1][1])&&(x[0][0]==x[2][2])&&(x[3][3]==x[0][0])&&x[0][0]=='O')
    cc=x[0][0];
    for (int i=0;i<4;i++)
    if ((x[0][3]==x[1][2])&&(x[0][3]==x[2][1])&&(x[3][0]==x[0][3])&&x[3][0]=='O')
    cc=x[0][3];
    
    x[p][k]='X';
    
    for (int i=0;i<4;i++)
    if ((x[i][0]==x[i][1])&&(x[i][1]==x[i][2])&&(x[i][3]==x[i][0])&&x[i][0]=='X')
    cc=x[i][0];
    for (int i=0;i<4;i++)
    if ((x[0][i]==x[1][i])&&(x[0][i]==x[2][i])&&(x[3][i]==x[0][i])&&x[0][i]=='X')
    cc=x[0][i];
    for (int i=0;i<4;i++)
    if ((x[0][0]==x[1][1])&&(x[0][0]==x[2][2])&&(x[3][3]==x[0][0])&&x[0][0]=='X')
    cc=x[0][0];
    for (int i=0;i<4;i++)
    if ((x[0][3]==x[1][2])&&(x[0][3]==x[2][1])&&(x[3][0]==x[0][3])&&x[3][0]=='X')
    cc=x[0][3];
    
    cout<<"Case #"<<i<<": ";
    if (cc!='0')
    cout<<cc<<" won"<<endl;
    else
    {
      int f=0;
          for (int i=0;i<4;i++)
    for (int j=0;j<4;j++)
    if (x[i][j]=='.')
    f=1;
      if (f==0)
      cout<<"Draw\n";
      else cout<<"Game has not completed\n";
     
    }
  }    
  return 0;
}
