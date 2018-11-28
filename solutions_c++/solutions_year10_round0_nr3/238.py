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
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef unsigned int UINT;

typedef struct
{
  int people;
  int next;
}T_ST;

T_ST array[1000];
int group[1000];

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,K,R;
    cin>>R;
    cin>>K;
    cin>>N;
//cout<<"N="<<N<<"  K="<<K<<endl;

    int n,r;
    for(n=0;n<N;n++)
    {
      cin>>group[n];
    }
    for(n=0;n<N;n++)
    {
      ll count = group[n];
      ll people = 0;
      int index = n;
      while(count<=K)
      {
        people = count;
        index = (index+1)%N;
        if(index == n)break;
        count+=group[index];
      }
      array[n].people = people;
      array[n].next = index;
    }
    ll result = 0;
    int index = 0;
    for(r=0;r<R;r++)
    {
      result += array[index].people;
      index = array[index].next;
    }

    cout<<"Case #"<<t<<": "<<result<<endl;
  }
  return 0;
}
