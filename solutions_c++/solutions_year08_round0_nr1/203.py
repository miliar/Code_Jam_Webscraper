#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int testCase,testNum;

int S,Q;

string engine[100];
string query[1000];

bool use[100];
int emptycnt;

int enginedx (const string &str)
{
  int L=0,R=S;
  while (L<R)
  {
    int m=(L+R)/2;
    if (str==engine[m])
      return m;
    if (str<engine[m])
      R=m;
    else
      L=m+1;
  }
  return -1;
}

int main()
{
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    cin>>S;
    cin.ignore(100,'\n');
    for (int i=0;i<S;++i)
      getline(cin,engine[i]);
    cin>>Q;
    cin.ignore(100,'\n');
    for (int i=0;i<Q;++i)
      getline(cin,query[i]);
    sort(engine,engine+S);
    int pos=0;
    int ans=0;
    while (true)
    {
      memset(use,false,sizeof(use));
      emptycnt=S;
      int i;
      for (i=pos;i<Q && emptycnt>0;++i)
      {
        int idx=enginedx(query[i]);
        if (!use[idx])
        {
          use[idx]=true;
          --emptycnt;
        }
      }
      if (emptycnt==0)
      {
        pos=i-1;
        ++ans;
      }
      else
        break;
    }
    cout<<"Case #"<<testCase<<": ";
    cout<<ans<<endl;
  }
}
