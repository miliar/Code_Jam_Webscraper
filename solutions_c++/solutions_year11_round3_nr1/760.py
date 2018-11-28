#include<iostream>
#include<string>
#include<vector>
using namespace std;

typedef vector<string> vs;

int main() {
  int t;
  cin>>t;
  for (int nc=1;nc<=t;++nc) {
    cout<<"Case #"<<nc<<':'<<endl;
    int r,c;
    cin>>r>>c;
    vs orig(r);
    for (int i=0;i<r;++i) cin>>orig[i];
    bool ok=true;
    for (int i=0;i<r and ok;++i) {
      for (int j=0;j<c and ok;++j) {
        if (orig[i][j]=='#') {
          ok=(i+1<r and j+1<c and orig[i][j+1]=='#' and orig[i+1][j]=='#' and orig[i+1][j+1]=='#');
          if (ok) {
            orig[i][j]='/';
            orig[i][j+1]='\\';
            orig[i+1][j]='\\';
            orig[i+1][j+1]='/';
          }
        }
      }
    }
    if (ok) {
      for (int i=0;i<r;++i) cout<<orig[i]<<endl;
    } else cout<<"Impossible"<<endl;
  }
}
