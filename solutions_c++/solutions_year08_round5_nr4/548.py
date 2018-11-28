#include <iostream>
using namespace std;

int testCase,testNum;
int H,W,R;

int dp[101][101];
bool rock[101][101];

int gdp (int x,int y)
{
  if (x>H || y>W)
    return -2;
  if (rock[x][y])
    return -2;
  if (x==H && y==W)
    return 1;
  int &ret=dp[x][y];
  if (ret!=-1)
    return ret;
  ret=0;
  int r1=gdp(x+1,y+2);
  if (r1!=-2)
    ret=(ret+r1)%10007;
  int r2=gdp(x+2,y+1);
  if (r2!=-2)
    ret=(ret+r2)%10007;
  return ret;
}

int main()
{
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    memset(rock,false,sizeof(rock));
    memset(dp,-1,sizeof(dp));
    cin>>H>>W>>R;
    for (int i=0;i<R;++i)
    {
      int a,b;
      cin>>a>>b;
      rock[a][b]=true;
    }
    cout<<"Case #"<<testCase<<": "<<gdp(1,1)<<endl;
  }
}
