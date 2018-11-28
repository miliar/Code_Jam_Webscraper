#include <iostream>

using namespace std;

int main(){
  int T;
  cin >> T;
  for (int i = 0; i < T; i++){
    int N, K;
    cin >> N >> K;
    int n = 1;
    for (int j = 0; j < N; j++){
      n *= 2;
    }
    if ((K % n) == n-1){
      cout << "Case #" << (i+1) << ": " << "ON" << endl;
    }else{
      cout << "Case #" << (i+1) << ": " << "OFF" << endl;
    }
  }
  return 0;
}
