#include<iostream>
#include<vector>
#include<string>
using namespace std;
#define MAX 100
#define MOD 10007
int grid[MAX][MAX];
long long soln[MAX][MAX];
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int H,W,R;
    cin>>H>>W>>R;
    for(int i=0;i<MAX;i++)
    for(int j=0;j<MAX;j++)
    grid[i][j]=soln[i][j]=0;
    for(int i=0;i<R;i++)
    { int a,b;
      cin>>a>>b;
      grid[a-1][b-1]=1;
    }
    soln[H-1][W-1]=1;
    for(int i=H-1;i>=0;i--)
    for(int j=W-1;j>=0;j--)
    if(i!=H-1&&j!=W-1)
    { soln[i][j]=0;
      if(grid[i][j]!=1)
      for(int k=0;k<3;k++)
      for(int l=0;l<3;l++)
      if(k*k+l*l==5&&i+k<H&&j+l<W)  
      soln[i][j]=(soln[i][j]+soln[i+k][j+l])%MOD;
    }  
    cout<<"Case #"<<t+1<<": "<<soln[0][0]<<"\n";
  }
}
