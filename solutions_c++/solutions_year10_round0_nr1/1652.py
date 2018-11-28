#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main() {
  ifstream fin("data.in");
  ofstream fout("data.out");
  int line_num;
  fin >> line_num;
  long long N, K;
  for (int i = 0; i < line_num; i++) {
    fin >> N >> K;
    if (K % (1UL << N) == ((1UL << N) - 1))
      fout << "Case #" << i + 1 << ": ON" << endl;
    else
      fout << "Case #" << i + 1 << ": OFF" << endl;
  }
  fout.close();
  fin.close();
}
