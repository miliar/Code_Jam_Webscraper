#include <iostream>
#include <vector>
using namespace std;
typedef long long LL;
void solve(){
  LL C;cin>>C;
  LL D;cin>>D;
  vector<LL> P(C);
  vector<LL> V(C);
  vector<LL> VT(C);
  for(int i=0;i<C;++i){
    cin>>P[i]>>V[i];
    if(i==0)VT[0]=V[0];
    else VT[i]=VT[i-1]+V[i];
  }
  LL res = 0;
  LL remain = -10000000;
  for(int i=0;i<C;++i){
    res=max(res,(V[i]-1)*D+max(0LL,remain+D-P[i]));
    remain=(V[i]-1)*D+max(P[i],remain+D);
  }
  cout << res/2.0 << endl;
}
int main(){
  int N;cin>>N;
  for(int i=1;i<=N;++i){
    cout << "Case #" << i <<": ";
    solve();
  }
  return 0;
}

