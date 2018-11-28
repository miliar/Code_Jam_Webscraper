#include <iostream>
#include <vector>
#include <string>

int main() {
  int T;
  std::cin >> T;
  for (int tcase = 1; tcase <= T; ++tcase) {
    int C;
    std::cin >> C;
    std::vector<char> es(26 * 26, '\0');
    for (int i = 0; i < C; ++i) {
      std::string s;
      std::cin >> s;
      es[26 * (s[0] - 'A') + (s[1] - 'A')] = s[2];
      es[26 * (s[1] - 'A') + (s[0] - 'A')] = s[2];
    }

    int D;
    std::cin >> D;
    std::vector<bool> ds(26 * 26, false);
    for (int i = 0; i < D; ++i) {
      std::string s;
      std::cin >> s;
      ds[26 * (s[0] - 'A') + (s[1] - 'A')] = true;
      ds[26 * (s[1] - 'A') + (s[0] - 'A')] = true;
    }

    int N;
    std::cin >> N;
    std::string X;
    std::cin >> X;

    std::string b;
    for (int i = 0; i < N; ++i) {
      char ch = X[i];
      //      std::cout << ch << " " << b << "\n";
      bool bleh = false;
      if (!b.empty()) {
	char bback = b.back();
	char repl = es[26 * (ch - 'A') + (bback - 'A')];
	if (repl) {
	  b.back() = repl;
	  bleh = true;
	}
      }
      if (!bleh) {
	for (int j = 0; j < b.size(); ++j) {
	  if (ds[26 * (b[j] - 'A') + (ch - 'A')]) {
	    b = "";
	    bleh = true;
	    break;
	  }
	}
      }
      if (!bleh) {
	b.push_back(ch);
      }
    }

    std::cout << "Case #" << tcase << ": [";
    for (int i = 0; i < b.size(); ++i) {
      if (i != 0) {
	std::cout << ", ";
      }
      std::cout << b[i];
    }
    std::cout << "]\n";
  }

}
