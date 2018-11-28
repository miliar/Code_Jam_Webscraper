#include <iostream>
#include <fstream>
#include <vector>
#include <string>

main(int argc, char *argv[])
{
  std::ifstream infile(argv[1]);
  int T, R, K, N;
  infile >> T;
  for (int i=0;i<T;i++) {
    infile >> R >> K >> N;
    std::vector<int> g(N);
    for (int j=0;j<N;j++)
      infile >> g[j];
    std::vector<int> sizes(N);
    std::vector<int> nexts(N);
    for (int j=0;j<N;j++) {
      int sz = g[j];
      int p = (j + 1)%N;
      while ((sz + g[p])<=K && p!=j) {
	sz += g[p];
	p = (p + 1)%N;
      }
      nexts[j] = p;
      sizes[j] = sz;
    }
    int p = 0;
    long long total = 0;
    for (int j=0;j<R;j++) {
      total += (long long)sizes[p];
      p = nexts[p];
    }
    std::cout << "Case #" << (i+1) << ": " << total << std::endl;
  }
}
