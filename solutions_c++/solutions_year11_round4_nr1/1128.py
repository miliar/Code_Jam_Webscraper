#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <utility>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FOR(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define REP(i,n) FOR(i,0,n)
#define all(c) (c).begin(), (c).end()
#define tr(container,it) \
    for(typeof((container).begin()) it = (container).begin(); it!=(container).end(); it++)

int main(){
  int T,tt=1;
  cin>>T;
  while(T--){
    double X,S,R,t,N;
    cin>>X>>S>>R>>t>>N;
    double a,b,c,tot=0;
    vector<pair<int,int> > ww;
    REP(i,N){
      cin>>a>>b>>c;
      ww.push_back(make_pair(c,b-a));
      tot+=b-a;
    }
    ww.push_back(make_pair(0,X-tot));
    sort(all(ww));
    
    double tottime=0;
    REP(i,N+1){
      a=ww[i].first;
      b=ww[i].second;
      double rtime = b/(a+R);
      double trun = min(rtime,t);
      tottime+=trun;
      b-=trun*(a+R);
      t-=trun;
      double wtime = b/(a+S);
      tottime+=wtime;
    }
    printf("Case #%d: %.9f\n",tt++,tottime);
    //    cout<<"Case #"<<tt++<<": "<<tottime<<endl;
  }
}
      

      
