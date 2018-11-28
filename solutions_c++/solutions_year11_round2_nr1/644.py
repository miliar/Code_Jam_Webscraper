#include <iostream>
#include <vector>
#include <string>
#include <boost/format.hpp>
using namespace std;

void solve(){
  int res = 0;
  int N;cin>>N;
  vector<string> st(N);
  for(int i=0;i<N;++i)cin>>st[i];
  vector<int> win(N);fill(win.begin(),win.end(),0);
  vector<int> games(N);fill(games.begin(),games.end(),0);
  vector<double> WP(N);
  vector<double> OWP(N);
  vector<double> OOWP(N);
  for(int i=0;i<N;++i){
    for(int j=0;j<N;++j){
      if(st[i][j]=='1')win[i]++;
      if(st[i][j]=='0'||st[i][j]=='1')games[i]++;
    }
    WP[i]=(double)win[i]/games[i];
    //cout<<"WP["<<i<<"]="<<WP[i]<<"="<<win[i]<<"/"<<games[i]<<endl;
  }
  for(int i=0;i<N;++i){
    double sum = 0;
    for(int j=0;j<N;++j){
      if(st[i][j]=='0'){
        sum+=(double)(win[j]-1)/(games[j]-1);
      }
      else if(st[i][j]=='1'){
        sum+=(double)(win[j])/(games[j]-1);
      }
    }
    OWP[i]=sum/games[i];
    //cout<<"OWP["<<i<<"]="<<OWP[i]<<"="<<sum<<"/"<<games[i]<<endl;
  }
  for(int i=0;i<N;++i){
    double sum = 0;
    for(int j=0;j<N;++j){
      if(st[i][j]=='0'||st[i][j]=='1'){
        sum+=OWP[j];
      }
    }
    OOWP[i]=sum/games[i];
    //cout<<"OOWP["<<i<<"]="<<OOWP[i]<<"="<<sum<<"/"<<games[i]<<endl;
  }
  for(int i=0;i<N;++i){
    cout << boost::format("%.10f")%(0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]) << endl;
  }
}
int main(){
  int N;cin>>N;
  for(int i=1;i<=N;++i){
    cout << "Case #" << i <<": "<<endl;
    solve();
  }
  return 0;
}


