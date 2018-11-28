
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOR(i,a,b) for(int i = (a) ; i < (b) ; i ++)
#define REP(i,n) FOR(i, 0, n)
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define pb push_back

void run()
{
  int a,b;
  double pro[100010];
  double num[100010];

  cin>>a>>b;
  REP(i,a)
    cin>>pro[i];
  memset(num, 0, sizeof(num));
  REP(i,a+1)
  {
    double p = 1.0;
    REP(j,i)
      p *= pro[j];
    if (i < a)
      p *= 1-pro[i];
    REP(j,a+1)
    {
      num[j] += p*(b-a+1+2*j);
      if (j < a-i)
        num[j] += p*(b+1);
    }
    num[a+1] += p*(2+b);
  }
  double m = 1000000;
  REP(i, a+2)
    if (m > num[i])
      m = num[i];

  printf("%0.6lf", m);

  return;
}

int main()
{
  int T;
  cin>>T;

  REP(k, T)
  {

    cout<<"Case #"<<k+1<<": ";

    run();

    cout<<endl;
  }

  return 0;
}
