#include<string>
#include<cmath>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
vector<int> decomp (int t)
{
  vector<int> ret;
  int a1=t/3;t-=a1;
  int a2=t/2,a3=t-a2;
  ret.push_back(max(a1,max(a2,a3)));
  if (a1==a2&&a2==a3)
    ret.push_back(1);
  else if ((a1==a2&&a1-a3==1)||(a1==a3&&a1-a2==1)||(a2==a3)&&a2-a1==1)
    ret.push_back(2);
  else if ((a1==a2&&a1-a3==-1)||(a1==a3&&a1-a2==-1)||(a2==a3)&&a2-a1==-1)
    ret.push_back(3);
  else if ((a1==a2&&a1-a3==2)||(a1==a3&&a1-a2==2)||(a2==a3)&&a2-a1==2)
    ret.push_back(4);
  else if ((a1==a2&&a1-a3==-2)||(a1==a3&&a1-a2==-2)||(a2==a3)&&a2-a1==-2)
    ret.push_back(5);
  return ret;
}
int main ()
{
  ifstream in ("B-large.in");
  ofstream out ("A.out");
  int T;in>>T;
  for (int i=1;i<T+1;++i)
  {
    if (i!=1)
      out<<endl;
    int N,S,P,t,count=0;
    in>>N>>S>>P;
    for (int j=0;j<N;++j)
    {
      in>>t;
      if (t==1||t==0)
      {
        if (t>=P)
          ++count;
      }
      else
      {
        vector<int> op=decomp(t);
        if (op[1]==1||op[1]==2)
        {
          if (op[0]+1==P&&S!=0)
          {
            ++count;--S;
          }
          else if (op[0]>=P)
            ++count;
        }
        else if ((op[1]==3||op[1]==4)&&op[0]>=P)
          ++count;
        else if (op[1]==5)
        {
          if (op[0]==P&&S!=0)
          {
            ++count;--S;
          }
          else if (op[0]-1>=P)
          {
            ++count;
          }
        }
      }
    }
    out<<"Case #"<<i<<": "<<count;
  }
  return 0;
}