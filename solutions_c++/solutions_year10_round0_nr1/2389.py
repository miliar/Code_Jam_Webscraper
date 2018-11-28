
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv) {
  if(argc != 2) {
    cout << "Missing filename" << endl;
    return -1;
  }

  ifstream fp(argv[1]);
  
  int T;
  fp >> T;

  for(int i = 0; i < T; i++) {
    int N;
    unsigned int K;
    fp >> N;
    fp >> K;
    
    unsigned int mask = 0;
    for(int j = 0; j < N; j++) {
      mask <<= 1;
      mask += 1;
    }

//    unsigned int state = K & mask;
    
    bool found_zero = false;
    for(int j = 0; j < N; j++) {
      if(K & 0x1) {
        K >>= 1;
      }
      else {
        found_zero = true;
      }
    }
    bool state = !found_zero;


//    cout << "Case #" << (i+1) << ": " << (state?"ON":"OFF") << "\tK:" << K << "\tN:" << N << "\tS:" << state << endl;
    cout << "Case #" << (i+1) << ": " << (state?"ON":"OFF") << endl;
  }

}

