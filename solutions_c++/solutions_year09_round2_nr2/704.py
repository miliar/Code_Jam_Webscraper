#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>

namespace {
  inline void next(std::string& n) {
    std::string x = n;
    std::next_permutation(x.begin(), x.end());
    if (n == x) {
      n = std::string("0") + n;
      x = n;
      std::next_permutation(x.begin(), x.end());
    }
    bool OK = true;
    for (int i = 0; i < n.length(); ++i) {
      if (x[i] < n[i]) {
        OK = false;
        break;
      } else if (x[i] > n[i]) {
        break;
      }
    }
    if (!OK) {
      n = std::string("0") + x;
      for (int i = 0; i < n.length(); ++i) {
        if (n[i] != '0') {
          n[0] = n[i];
          n[i] = '0';
          break;
        }
      }
    } else {
      n = x;
    }
  }
}

int main(int argc, char *argv[]) {
	if (argc < 2) return 1;
	std::ifstream infile(argv[1]);
	int nlines;
	infile >> nlines;
	std::string line;
	std::getline(infile, line);
	for (int i = 1; i <= nlines; ++i) {
    std::string n;
    infile >> n;
    //std::cerr << n << " ";
    next(n);
    //std::cerr << n << "\n";

		std::cout << "Case #" << i << ": " << n << "\n";
	}
	return 0;
}

