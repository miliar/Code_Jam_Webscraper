#include <iostream>
using namespace std;


int main(int argc, char *argv[]) {
  int T, N, K; 
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    cin >> N >> K >> ws;
    if((K+1) % (1<<N) == 0) {
      cout << "Case #" << t << ": " << "ON" << endl;
    } else {
      cout << "Case #" << t << ": " << "OFF" << endl;
    }
  }
  return 0;
}
