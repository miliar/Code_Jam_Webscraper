#include <iostream>
#include <fstream>
#include <vector>
#include <string>

main(int argc, char *argv[])
{
  std::ifstream infile(argv[1]);
  int T, N, K;
  infile >> T;
  for (int i=0;i<T;i++) {
    infile >> N >> K;
    std::cout << "Case #" << i+1 << ": ";
    if (!((K+1) % (1<<N)))
      std::cout << "ON" << std::endl;
    else
      std::cout << "OFF" << std::endl;
  }
}
