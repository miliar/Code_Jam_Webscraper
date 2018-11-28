#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
#define REP(i,n) for(i=0;i<n;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define int64 long long

using namespace std;

int64 t,tt,i,j,k,c;
string s;
vector<int> ss;
int64 dd[300];
int64 cc[50];
int64 x,sum;

int main(){
  freopen("1ca.in","r",stdin);
  freopen("1ca.out","w",stdout);
  i=0;
  FOR(j,0,35){
    cc[i++]=j;
  }
  cc[0]=1; cc[1]=0;
  cin >> t;
  REP(tt,t){
    cin >> s;
    ss.clear();
    memset(dd,0,sizeof(dd));
    REP(i,s.length()){
      ss.push_back(s[i]-0);
    }
    c=0;
    REP(i,s.length()){
      if (dd[s[i]-0]==0){
        dd[s[i]-0]=1;
        FOR(j,i,s.length()-1){
          if (s[j]==s[i]){
            ss[j]=cc[c];
          }
        }
        ++c;
      }
    }
    x=1;
    sum=0;
    if (c==1) c=2;
    for(i=s.length()-1;i>=0;--i){
      sum+=ss[i]*x;
      x*=c;
    }
    cout << "Case #" << tt+1 << ": " << sum << endl;
  }
}
