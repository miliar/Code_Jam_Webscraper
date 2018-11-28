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

vector<PI> node;

int main(void)
{
  int T,t;
  cin>>T;
//cout<<"T="<<T<<endl;
  for(t=1;t<=T;t++)
  {
//cout<<"t="<<t<<endl;
    int i,j;
    int N;
    int n;
    cin>>N;
    node.clear();
//cout<<"N="<<N<<"  M="<<M<<endl;
    for(n=0;n<N;n++)
    {
      int tmp0;
      int tmp1;
      cin>>tmp0;
      cin>>tmp1;
      node.push_back(make_pair(tmp0,tmp1));
    }
    int ret = 0;
    for(i=0;i<N;i++)
    {
      int xi = node[i].first;
      int yi = node[i].second;
      for(j=i+i;j<N;j++)
      {
        int xj = node[j].first;
        int yj = node[j].second;
        if((xi-xj)*(yi-yj)<0)
        {
          ret++;
        }
      }
    }
    cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}
