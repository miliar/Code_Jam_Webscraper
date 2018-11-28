#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char **argv) {
  fstream f(argv[1], fstream::in);
  int T,N,K;
  f >> T;
  for (int i=1; i<=T; i++) {
    f >> N >> K;
    cout << "Case #" << i << ": ";
    int mask = (1<<N)-1;
    if ( (K & mask) == mask)
      cout << "ON" << endl;
    else
      cout << "OFF" << endl;
  }
  
  return 0;
}
