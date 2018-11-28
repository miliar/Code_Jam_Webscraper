#include <iostream>
#include <fstream>
#include <vector>
#include <string>

main(int argc, char *argv[])
{
  std::ifstream infile(argv[1]);
  int T, N;
  infile >> T;
  for (int t=0;t<T;t++) {
    infile >> N;
    std::vector<int> A(N), B(N);
    int numInt = 0;
    for (int i=0;i<N;i++) {
      infile >> A[i] >> B[i];
      for (int j=0;j<i;j++) {
	if ((A[i]-A[j])*(B[i]-B[j])<0) 
	  numInt++;
      }
    }
    std::cout << "Case #" << (t+1) << ": " << numInt << std::endl;
  }
}
