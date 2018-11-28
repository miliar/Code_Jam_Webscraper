#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
using namespace std;
int main(){
  int T, n;
  long long x[850];
  long long y[850];
  int c=1;
  cin>>T;
  while(T--){
    long long r=0;
    cin>>n;
    for(int i=0; i<n; i++)
      cin>>x[i];
    for(int i=0; i<n; i++)
      cin>>y[i];
    sort(x,x+n);
    sort(y,y+n);
    for(int i=0; i<n; i++){
	r+=x[i]*y[n-i-1];
      }
    cout<<"Case #"<<c++<<": "<<r<<endl;
  }
}
