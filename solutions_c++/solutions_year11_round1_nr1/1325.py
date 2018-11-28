#include <iostream>
#include <vector>
using namespace std;

void solve(){
  int res = 0;
  int N, PD, PG;
  cin>>N>>PD>>PG;

  int DW= PD;
  int DL=100-PD;
  for(int i=2;i<=100;++i){
    while(DW%i==0&&DL%i==0){
      DW/=i;
      DL/=i;
    }
  }
  if(DW+DL>N){
    cout << "Broken" << endl;
    return;
  }
  int GW= PG;
  int GL=100-PG;
  if((DW>0&&GW==0)||(DL>0&&GL==0)){
    cout << "Broken" << endl;
    return;
  }
  cout << "Possible" << endl;
}
int main(){
  int N;cin>>N;
  for(int i=1;i<=N;++i){
    cout << "Case #" << i <<": ";
    solve();
  }
  return 0;
}

