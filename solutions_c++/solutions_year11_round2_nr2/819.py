#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

int main() {
  cout.setf(ios::fixed);
  cout.precision(1);
  int t;
  cin>>t;
  for (int nc=1;nc<=t;++nc) {
    cout<<"Case #"<<nc<<": ";
    int c,d;
    cin>>c>>d;
    vi pos(c),num(c);
    for (int i=0;i<c;++i) cin>>pos[i]>>num[i];
    ll maxim=-1,move=d*(num[0]-1);
    for (int i=1;i<c;++i) {
      if (move>maxim) maxim=move;
      move+=d+pos[i-1]-pos[i];
      if (move<0) move=0;
      move+=d*(num[i]-1);
    }
    if (move>maxim) maxim=move;
    cout<<maxim/2.<<endl;
  }
}
