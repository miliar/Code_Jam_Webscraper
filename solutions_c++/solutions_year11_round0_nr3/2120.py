#include <iostream>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int n,res=0,min=9999999,can=0;
    cin>>n;
    for(int i=0;i<n;i++){
      int a;
      cin>>a;
      if(a<min)
	min=a;
      res+=a;
      can ^= a;
    }
    res -= min;
    cout << "Case #" << t << ": ";
    if(!can)
      cout << res << endl;
    else
      cout << "NO" << endl;
  }
  
  return 0;
}
