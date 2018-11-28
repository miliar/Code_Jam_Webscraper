#include<iostream>
#include<algorithm>
using namespace std;

int GCD(int a, int b){
  return b == 0 ? a : GCD(b, a%b);
}

int main(){
  
  int C;
  cin >> C;
  for(int c = 1; c <= C; c++){
    int N;
    int a, b, diff, gcd;
    cin >> N;
    cin >> a >> b;
    gcd = abs(a - b);
    for(int i = 2; i < N; i++){
      a = b;
      cin >> b;
      diff = abs(a - b);
      gcd = GCD(max(diff, gcd), min(diff, gcd));
    }
    cout << "Case #" << c << ": " << (gcd <= 1 ? 0 : 
				      (a%gcd ? gcd - a%gcd : 0)) << endl;
  }

  return 0;
}
