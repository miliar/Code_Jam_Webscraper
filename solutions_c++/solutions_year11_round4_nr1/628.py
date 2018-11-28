#include <iostream>
#include <vector>
#include <algorithm>
#include <boost/format.hpp>
using namespace std;

void solve(){
  int X,S,R,N;
  double t;
  cin>>X>>S>>R>>t>>N;
  //cout<<X<<":"<<S<<":"<<R<<":"<<t<<":"<<N<<endl;
  vector<int> B(N);
  vector<int> E(N);
  vector<int> w(N);
  for(int i=0;i<N;++i)cin>>B[i]>>E[i]>>w[i];
  vector<pair<double,double>> ps;
  int prev=0;
  for(int i=0;i<N;++i){
    ps.push_back(make_pair(0,B[i]-prev));prev=B[i];
    ps.push_back(make_pair(w[i],E[i]-prev));prev=E[i];
  }
  ps.push_back(make_pair(0,X-prev));
  sort(ps.begin(),ps.end());
  double res = 0;
  for(int i=0;i<ps.size();++i){
    if(ps[i].second<=(ps[i].first+R)*t){
      res+=ps[i].second/(ps[i].first+R);
      t-=ps[i].second/(ps[i].first+R);
    }else{
      res+=t;
      res+=(ps[i].second-t*(ps[i].first+R))/(ps[i].first+S);
      t=0;
    }
    //cout << ps[i].first << ":" << ps[i].second<<", "<<res<<", "<<t<<endl;
  }
  cout << boost::format("%.10f")%res << endl;
}
int main(){
  int N;cin>>N;
  for(int i=1;i<=N;++i){
    cout << "Case #" << i <<": ";
    solve();
  }
  return 0;
}


