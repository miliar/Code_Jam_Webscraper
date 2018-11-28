#include <iostream>
using namespace std;
int main(){
  int T;
  cin >> T;
  for(int Case=1; Case <= T; ++Case){
    int sum = 0;
    int xor = 0;
    int minim = INT_MAX;
    int N;
    cin >> N;
    while(N--){
      int C;
      cin >> C;
      sum += C;
      xor ^= C;
      minim = min(minim, C);
      //cerr << "C: " << C << " sum: " << sum << " xor: " << xor << " minim: " << minim << endl;
    }
    cout << "Case #" << Case <<": ";
    if(xor!=0)
      cout << "NO";
    else
      cout << sum - minim;
    cout << endl;
  }
  return 0;
}