#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char **argv) {

  char *filename = argv[1];

  ifstream file(filename);

  int T;

  file >> T;

  int N, K;

  for (int i = 0; i < T; i++) {
    file >> N;
    file >> K;

    int pot = (int)pow(2,N);
    if ((K+1) % pot == 0) {
      cout << "Case #" << (i+1) << ": ON" << endl;
    } else {
      cout << "Case #" << (i+1) << ": OFF" << endl;
    }
  }

  file.close();
}
