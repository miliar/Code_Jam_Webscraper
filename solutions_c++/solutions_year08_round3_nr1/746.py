#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define SORTC(c,cmp) sort(ALL(c),cmp)
#define SORT(c) sort(ALL(c))
#define PB push_back
#define PF push_front
#define SZ size()

#define PI acos(-1.)

typedef long long int LL;

int main()
{
  int numCase;
  cin>>numCase;
  REP(case_,numCase)
  {
    vector<LL> freq;
    LL P,K,L,tmp,ans=0;
    cin>>P>>K>>L;
    REP(i,L) 
    {
      cin>>tmp;
      freq.PB(tmp);
    }
    SORT(freq);
    reverse(ALL(freq));

//    FORE(freq,i) cout<<*i<<' ';
//    cout<<endl;

    int press=0;
    REP(i,freq.SZ)
    {
      if(i%K==0) press++;
      ans+=freq[i]*press;
    }
    printf("Case #%d: %d\n", case_+1,ans);
  }
}
