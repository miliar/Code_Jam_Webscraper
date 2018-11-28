#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define SORT(c) sort((c).begin(),(c).end());
#define REVERSE(c) reverse((c).begin(),(c).end());
#define SZ size()
#define PI acos(-1.)


typedef unsigned long long int ULL;
typedef long long int LL;


int main()
{
  int T;
  cin>>T;
  REP(cs,T)
  {
    int dim;
    cin>>dim;

    vector<LL> v1,v2;

    LL t;
    REP(i,dim) 
    {
      cin>>t;v1.PB(t);
    }
    REP(i,dim) 
    {
      cin>>t;v2.PB(t);
    }
    
    SORT(v1);
    SORT(v2);
    REVERSE(v2);

    LL ans = 0;
    REP(i,v1.SZ)
    {
      ans+=v1[i]*v2[i];
    }

    printf("Case #%d: %ld\n",cs+1, ans);
  }
  return 0;
}
