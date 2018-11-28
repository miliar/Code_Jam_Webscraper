#include <iostream>
using namespace std;

/*
 * 0 0 a b c d
 * ad-bc=M
 */

int main(){
  int C;
  cin>>C;
  for(int c=1; c<=C; c++){
    cout<<"Case #"<<c<<": ";
    int A,N,M;
    cin>>N>>M>>A;
    if(A>N*M){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      int d=(A+N-1)/N;
      int c=N*d-A;
      cout<<0<<" "<<0<<" "<<N<<" "<<1<<" "<<c<<" "<<d<<endl;
    }
  }
  return 0;
}
