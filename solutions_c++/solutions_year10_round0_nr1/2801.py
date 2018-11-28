#include<iostream>
using namespace std;
unsigned long long int n,k1,k2;

bool Solve(){
  cin >> k1 >> k2;
  unsigned long long int cost=(1<<k1)-1;
  //  cout << k2 << endl;
  // cout << cost << ' '  << (int)(cost&k2) << endl;
  if((unsigned long long int)(cost&k2)==cost)return true;
  return false;
}
  
int main(){
  cin >> n;
  for(int i=0 ; i<n ; i++){
    cout << "Case #" << i+1 << ": ";
    if(Solve())cout << "ON" << endl;
    else cout << "OFF" << endl;
  }
  return 0;
}


