#include <iostream>
using namespace std;

long pow(int base, int exp)
{
    int ret = 1, i;
    for(i = 0; i < exp; i++){
          ret *= base;
    }
    return ret;
}

int main()
{
  int T, t;
  cin >> T;
  for(t = 1; t <= T; t++){
    long N, K;
    cin >> N >> K;
    long factor = pow(2, N);
    if(K % factor == factor - 1){
      cout << "Case #" << t << ": ON" << endl;
    } else {
      cout << "Case #" << t << ": OFF" << endl;
    }
  }
  return 0;
}

