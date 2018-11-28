#include<iostream>
#include<string>
#include<vector>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<string> vs;

int main() {
  cout.setf(ios::fixed);
  cout.precision(12);
  int t;
  cin>>t;
  for (int nc=1;nc<=t;++nc) {
    cout<<"Case #"<<nc<<':'<<endl;
    int n;
    cin>>n;
    vs data(n);
    for (int i=0;i<n;++i) cin>>data[i];
    vvi num(n,vi(n,-1)),den(n,vi(n,1));
    for (int i=0;i<n;++i) {
      int w=0,l=0;
      for (int j=0;j<n;++j) {
        if (data[i][j]=='1') ++w;
        else if (data[i][j]=='0') ++l;
      }
      for (int j=0;j<n;++j) {
        if (data[i][j]=='1') {
          num[i][j]=w-1;
          den[i][j]=w+l-1;
        } else if (data[i][j]=='0') {
          num[i][j]=w;
          den[i][j]=w+l-1;
        }
      }
      num[i][i]=w;
      den[i][i]=w+l;
    }
    vd owp(n,0);
    for (int i=0;i<n;++i) {
      int opps=0;
      for (int j=0;j<n;++j) {
        if (data[i][j]!='.') {
          owp[i]+=1.*num[j][i]/den[j][i];
          ++opps;
        }
      }
      owp[i]/=opps;
    }
    vd oowp(n,0);
    for (int i=0;i<n;++i) {
      int opps=0;
      for (int j=0;j<n;++j) {
        if (data[i][j]!='.') {
          oowp[i]+=owp[j];
          ++opps;
        }
      }
      oowp[i]/=opps;
    }
    for (int i=0;i<n;++i) {
      double res=0.25*num[i][i]/den[i][i]+owp[i]/2+oowp[i]/4;
      cout<<res<<endl;
    }
  }
}
