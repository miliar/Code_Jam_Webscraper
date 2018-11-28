#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;

//#define DEBUG_PRINT

int M[1<<10];
int cost[1<<10];

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int P;
    cin>>P;
    int all = 1<<P;
//cout<<"N="<<N<<"  K="<<K<<endl;
    int i,j;
    int rest = 0;
    for(i=0;i<all;i++)
    {
      int x;
      cin>>x;
      M[i] = P - x;
      rest += M[i];
    }
    for(i=0;i<(all-1);i++)
    {
      cin>>cost[i];
    }
    int min_cost = 0;
    int width = all;
    int num = 1;
    while(rest > 0)
    {
      int n;
      int index = 0;
      for(n=0;n<num;n++)
      {
        //>0の試合があるかどうかチェック
        int flag = 0;
        for(i=0;i<width;i++)
        {
          if(M[n*width + i]>0)
          {
            flag = 1;
            break;
          }
        }
        if(flag)
        {
          //1つ購入
          min_cost++;
          for(i=0;i<width;i++)
          {
            if(M[n*width + i]>0)
            {
              rest--;
              M[n*width + i]--;
            }
          }
        }
      }
      num<<=1;
      width>>=1;
    }
    cout<<"Case #"<<t<<": "<<min_cost<<endl;
  }
  return 0;
}
