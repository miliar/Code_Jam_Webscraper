#include <iostream>
using namespace std;

int main(){
int T,N,K;
bool p;
cin>>T;
for(int i=0;i<T;i++){
  cin>>N;
  cin>>K;
  p=true;
  for(int j=0;j<N;j++){
    if (K%2==0){
       p=false;
       break;
    }
    K=K/2;
  }
  cout<<"Case #"<<i+1<<": ";
  if (p)
    cout<<"ON"<<endl;
  else
    cout<<"OFF"<<endl;
    
}

}
