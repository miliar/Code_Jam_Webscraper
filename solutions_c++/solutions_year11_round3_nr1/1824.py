#include <iostream>
#include <string>
#include <vector>

typedef std::vector<char> vc;
typedef std::vector<vc> vvc;
int main()
{
  int T;
  std::cin >> T;

  for (int t = 1; t <= T; ++t) {
    int R, C;
    std::cin >> R >> C;

    vvc table;
    for (int r = 0; r < R; ++r) {
      vc row;
      std::string s;
      std::cin >> s;

      for (int c = 0; c < C; ++c) {
	row.push_back(s[c]);
      }

      table.push_back(row);
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
	if (table[r][c] == '#') {
	  if (r == R - 1 || c == C - 1 ||
	      table[r][c + 1] != '#' ||
	      table[r + 1][c] != '#' ||
	      table[r + 1][c + 1] != '#') {

	    std::cout << "Case #" << t << ":\nImpossible" << std::endl;
	    goto next_try;
	  }
	  table[r][c] = '/';
	  table[r][c + 1] = '\\';
	  table[r + 1][c] = '\\';
	  table[r + 1][c + 1] = '/';
	}
      }
    }

    std::cout << "Case #" << t << ":";
    for (int r = 0; r < R; ++r) {
      std::cout << "\n";
      for (int c = 0; c < C; ++c) {
	std::cout << table[r][c];
      }
    }
    std::cout << std::endl;
    
  next_try:
    ;
  }
}
