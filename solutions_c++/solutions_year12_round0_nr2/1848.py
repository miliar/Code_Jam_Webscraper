#include<iostream>
using namespace std;
int solve(){
  int n,s,p;
  cin >> n >> s >> p;
  int a=0;
  int b=0;
  for(int i=0;i<n;++i){
    int x;
    cin >> x;
    int r = (x+2)/3;
    if(r>=p){
      a++;  
    }else if(r==p-1 && x>=2 && x<=28 && (x%3!=1)){
      b++;
    }
  }
  return a + min(b,s);
}
int main(){
  int t;
  cin >> t;
  for(int i=1;i<=t;++i){
    cout << "Case #" << i << ": " << solve() << endl;
  }
}