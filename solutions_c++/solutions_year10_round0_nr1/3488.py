// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4
// Snappers

#include <iostream>
#include <fstream>

using namespace std;

unsigned T = 0, N = 0, K = 0;

int main(int argc, const char *argv[])
{
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " fielname" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }

  input >> T;
  
  for (unsigned t = 0; t < T; ++t) {
    input >> N >> K;

    int power = (1 << N) - 1;
    K %= 1 << N;
    cout << "Case #" << t + 1 << ": " << ((K == power) ? "ON" : "OFF") << "\n";
  }

  cout.flush();
  return 0;
}
