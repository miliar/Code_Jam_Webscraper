#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

int gcd(long long u, long long v){
    if(v==0) return u;
    return gcd(v,u%v);
}

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    long long res=0;
    long long n, l, h;
    bool ok=false;
    cin>>n>>l>>h;
    
    vector<long long> p(n);
    for(int i=0;i<n;++i){
      cin>>p[i];
    }
    
    if(l==1){
      ok=true;
      res=1;
    } else {
      
      for(int i=l;i<=h;++i){
        bool del=true;
        for(int j=0;j<n;++j){
          if(i%p[j]==0 || p[j]%i==0){;}
          else del=false;
        }
        if(del==true){
          ok=true;
          res=i;
          break;
        }
      }
      
    }
    
        
    cout<<"Case #"<<t<<": ";
    if (!ok) {cout<<"NO\n";}
    else {
       cout<<res<<endl;
    }
  }
  return 0;
}