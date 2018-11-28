#include<string>
#include<iostream>
using namespace std;

int T,N,ci;
int main(){
  cin >> T;
  for(int t=1;t<=T;t++){
    long long small = 9999999, sum = 0;
    unsigned int x = 0;
    cin >> N;
    for(int n=0;n<N;n++){
      cin >> ci;
      x = x xor ci;
      if( ci < small ){
	small = ci;
      }
      sum += ci;
    }
    if(x==0){
      cout << "Case #" << t << ": " << sum-small << endl;
    } else {
      cout << "Case #" << t << ": NO" << endl;
    }
  }
}
