#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define SORT(c) sort((c).begin(),(c).end());
#define SZ size()

using namespace std;

int time2min(string s)
{
  int hh=atoi(s.substr(0,2).c_str());
  int mm=atoi(s.substr(3,2).c_str());
  return hh*60+mm;
}

int main()
{
  string t;
  int T;
  cin>>T;
  REP(c,T)
  {
    vector<int> dA, aA, dB, aB;
    int turn,NA,NB;
    cin>>turn>>NA>>NB;

    REP(i,NA)
    {
      cin>>t; dA.PB(time2min(t));
      cin>>t; aA.PB(time2min(t)+turn);
    }

    REP(i,NB)
    {
      cin>>t; dB.PB(time2min(t));
      cin>>t; aB.PB(time2min(t)+turn);
    }

    SORT(dA); SORT(aA); SORT(dB); SORT(aB);

//    FORE(dA,i) cout<<*i<<endl;
//    FORE(aA,i) cout<<*i<<endl;
//    FORE(dB,i) cout<<*i<<endl;
//    FORE(aB,i) cout<<*i<<endl;

    int startA=dA.SZ;
    for(int i=0,j=0;i<dA.SZ&&j<aB.SZ;++i)
      if(aB[j]<=dA[i]) ++j, --startA;

    int startB=dB.SZ;
    for(int i=0,j=0;i<dB.SZ&&j<aA.SZ;++i)
      if(aA[j]<=dB[i]) ++j, --startB;

    printf("Case #%d: %d %d\n",c+1, startA, startB);
  }
}
