#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main() {
  int T; fin >> T;
  for (int t = 0; t < T; t++) {
    int N, Pd, Pg;
    fin >> N >> Pd >> Pg;
    if (Pg == 0) {
      if (Pd > 0)
        fout << "Case #" << t + 1 << ": Broken\n";
      else 
        fout << "Case #" << t + 1 << ": Possible\n";
    }
    else if (Pg == 100) {
      if (Pd == 100)
        fout << "Case #" << t + 1 << ": Possible\n";
      else 
        fout << "Case #" << t + 1 << ": Broken\n";
    }
    else {
      int n = Pd, m = 100;
      int prime[] = {2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
      for (int i = 0; i < sizeof(prime)/sizeof(prime[0]); ++i) {
        int p = prime[i]  ;
        while (n % p == 0 && m % p == 0) { n /= p; m /= p; }
      }
      if (m <= N)
        fout << "Case #" << t + 1 << ": Possible\n";
      else
        fout << "Case #" << t + 1 << ": Broken\n";
    }
  }
	return 0;
}
