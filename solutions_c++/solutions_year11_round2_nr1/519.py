#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define fr(i,c) for(__typeof (c.begin()) i=c.begin(); i!=c.end(); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long ll;

int win[100],game[100];
double wp[100],owp[100],oowp[100];

int main(){
  int T; cin>>T;
  rep(cs,T){
    int n; cin>>n;
    string s;
    vector<string> res;
    rep(i,n)cin>>s,res.pb(s);

    rep(i,n)win[i]=game[i]=0;

    rep(i,n){
      rep(j,n)if(res[i][j]!='.'){
        game[i]++;
        if(res[i][j]=='1')win[i]++;
      }
      wp[i]=win[i]*1.0/game[i];
    }
    rep(i,n){
      int o=0; double sum=0;
      rep(j,n)if(res[i][j]!='.'){
        o++;
        sum+=res[i][j]=='1'?
          win[j]*1.0/(game[j]-1):(win[j]-1.0)/(game[j]-1);
      }
      owp[i]=sum/o;
    }
    rep(i,n){
      int o=0; double sum=0;
      rep(j,n)if(res[i][j]!='.'){
        o++;
        sum+=owp[j];
      }
      oowp[i]=sum/o;
    }
    //rep(i,n)cerr<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;

    cout<<"Case #"<<cs+1<<":"<<endl;
    rep(i,n)printf("%.7f\n",0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
  }
  return 0;
}
