#include <iostream>
#include <fstream>
#include <cmath>

main(int argc, char *argv[])
{
  std::ifstream infile(argv[1]);
  int T, L, P, C;
  infile >> T;
  for (int t=0;t<T;t++) {
    infile >> L >> P >> C;
    int N = 0;    
    while (L<P) {
      L *= C;
      N++;
    }
    int n = 1;
    int c = 0;
    while (n<N) {
      n *= 2;
      c ++;
    }
    std::cout << "Case #" << (t+1) << ": " << c << std::endl;
  }
}
