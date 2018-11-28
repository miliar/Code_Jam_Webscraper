#include <iostream>
#include <algorithm>
using namespace std;

int testCase,testNum;

int M;
bool V;

struct Node
{
  bool value;
  char gate;
  bool change;
};

Node tree[10000];

int dp[10000][2];

int gdp (int pos,bool target)
{
  if (pos>=(M-1)/2)
    if (tree[pos].value==target)
      return 0;
    else
      return -2;
  int &ret=dp[pos][target];
  if (ret!=-1)
    return ret;
  ret=0x7f7f7f7f;
  for (int i=0;i<2;++i)
    for (int j=0;j<2;++j)
      if (tree[pos].gate=='&' && ((i&j)==target) || tree[pos].gate=='|' && ((i|j)==target))
      {
        int r1=gdp(pos*2+1,i);
        int r2=gdp(pos*2+2,j);
        if (r1!=-2 && r2!=-2)
          ret=min(ret,r1+r2);
      }
  if (tree[pos].change)
    for (int i=0;i<2;++i)
      for (int j=0;j<2;++j)
        if (tree[pos].gate=='&' && ((i|j)==target) || tree[pos].gate=='|' && ((i&j)==target))
        {
          int r1=gdp(pos*2+1,i);
          int r2=gdp(pos*2+2,j);
          if (r1!=-2 && r2!=-2)
            ret=min(ret,r1+r2+1);
        }
  if (ret==0x7f7f7f7f)
    ret=-2;
  return ret;
}

int main()
{
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    cin>>M;
    cin>>V;
    for (int i=0;i<(M-1)/2;++i)
    {
      int G,C;
      cin>>G>>C;
      if (G==1)
        tree[i].gate='&';
      else
        tree[i].gate='|';
      tree[i].change=(C==1);
    }
    for (int i=0;i<(M+1)/2;++i)
      cin>>tree[i+(M-1)/2].value;
    memset(dp,-1,sizeof(dp));
    int ans=gdp(0,V);
    cout<<"Case #"<<testCase<<": ";
    if (ans==-2)
      cout<<"IMPOSSIBLE"<<endl;
    else
      cout<<ans<<endl;
  }
}
