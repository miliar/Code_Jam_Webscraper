#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");

int main() {
  long long num;
  long long dig;
  long long input;
  fin >> num;
  for (int i = 0; i < num; i++) {
    fin >> dig >> input;
    if ((input % (0x1 << dig)) + 1 == (0x1 << dig)) {
      fout << "Case #" << i+1 << ": ON" << endl;
    }
    else {
      fout << "Case #" << i+1 << ": OFF" << endl;
    }
  }
  return 0;
}
