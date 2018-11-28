#include <iostream>
#include <vector>

int main() {
  int T;
  std::cin >> T;
  
  for (int tcase = 1; tcase <= T; ++tcase) {
    int N;
    std::cin >> N;

    std::vector<std::pair<int, int> > o_goals;
    std::vector<std::pair<int, int> > b_goals;
    for (int i = 0; i < N; ++i) {
      char c;
      std::cin >> c;
      int p;
      std::cin >> p;
      if (c == 'O') {
	o_goals.push_back(std::make_pair(p, i));
      } else {
	b_goals.push_back(std::make_pair(p, i));
      }
    }

    int o_pos = 1;
    int b_pos = 1;
    int o_achieve = 0;
    int b_achieve = 0;
    int o_sz = o_goals.size();
    int b_sz = b_goals.size();

    int j = 0;
    int count = 0;
    while (o_achieve != o_sz || b_achieve != b_sz) {
      //      std::cout << "o_pos " << o_pos << " b_pos " << b_pos << " j " << j << "\n";
      int incr_j = 0;
      if (o_achieve != o_sz) {
	if (o_goals[o_achieve].first == o_pos) {
	  if (o_goals[o_achieve].second == j) {
	    o_achieve++;
	    incr_j = 1;
	  }
	} else {
	  o_pos += (o_pos < o_goals[o_achieve].first ? 1 : -1);
	}
      }

      if (b_achieve != b_sz) {
	if (b_goals[b_achieve].first == b_pos) {
	  if (b_goals[b_achieve].second == j) {
	    b_achieve++;
	    incr_j = 1;
	  }
	} else {
	  b_pos += (b_pos < b_goals[b_achieve].first ? 1 : - 1);
	}
      }

      j += incr_j;
      ++count;
    }

    std::cout << "Case #" << tcase << ": " << count << "\n";
  }
}
