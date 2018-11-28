#include <iostream>
#include <string>
using namespace std;

int T,N,K;
int main(){
  cin >> T;
  for( int c=1; c<=T; c++ ){
    cin >> N >> K;
    cout << "Case #" << c << ": " << ( K % (1 << N) == (1 << N) - 1 ? "ON" : "OFF" ) << endl;
  }
}
