#include <iostream>
#include <algorithm>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
using namespace std;

#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ALL(s) s.begin(),s.end()
#define SZ(s) signed(s.size())
#define FOZ(i,v) FOR(i,SZ(v))
#define LET(a,b) typeof(b) a=b
#define FOREACH(it,s) for(LET(it,s.begin());it!=s.end();++it)
#define MP make_pair
typedef pair<int,int> PII;
typedef pair<int,char> PIC;
const int INF = 2000000000;

typedef long double ld;
typedef long long ll;

#define D(A) A

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum,ncases) {
    string s; cin>>s;
    //cerr<<s<<endl;
    set<char> c(ALL(s));
    map<char, int> v;
    int last = 0;
    ll b=max(SZ(c),2);
    ll ans=0;
    FOZ(i,s) {
      if(i==0) {
        v[s[i]] = 1;
      } else {
        if(not(v.count(s[i]))) {
          if(last==1) ++last;
          v[s[i]]=last++;
        }
      }
      //cerr<<v[s[i]];
      ans=ans*b + v[s[i]];
      //cerr<<"("<<ans<<")";
    }
    //cerr<<", base "<<b;
    //cerr<<endl;

    printf("Case #%d: ", casenum+1);
    cout<<ans<<endl;
  }
  return 0;
}
