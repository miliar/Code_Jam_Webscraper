#include <iostream>
#include <utility>
#include <map>
#include <string>
#include <list>
#include <vector>
#include <set>

typedef std::pair<char, char> elempair_t;
typedef std::map<elempair_t, char> combinemap_t;
typedef std::multimap<char, char> oppositemap_t;
typedef std::set<char> elemset_t;
typedef std::list<char> charlist_t;

void printchars(const charlist_t & list) {
  for (charlist_t::const_iterator it = list.begin(); it != list.end(); ++it) {
    std::cout << *it;
  }
  std::cout << "\n";
}

int main() {

  unsigned int T;
  std::cin >> T;

  for (unsigned int t = 0; t < T; ++t) {
    //std::cout << "new T\n";
    unsigned int C;
    std::cin >> C;

    combinemap_t combine_map;

    for (unsigned int c = 0; c < C; ++c) {
      std::string combstring;
      std::cin >> combstring;
      combine_map[std::make_pair(combstring[0], combstring[1])] = combstring[2];
      combine_map[std::make_pair(combstring[1], combstring[0])] = combstring[2];
    }

    unsigned int D;
    std::cin >> D;

    oppositemap_t opposite_map;

    for (unsigned int d = 0; d < D; ++d) {
      std::string opstring;
      std::cin >> opstring;
      opposite_map.insert(std::make_pair(opstring[0], opstring[1]));
      opposite_map.insert(std::make_pair(opstring[1], opstring[0]));
      //std::cout << "opposite " << opstring << "\n";
    }

    unsigned int N;
    std::cin >> N;

    charlist_t charlist;

    for (unsigned int n = 0; n < N; ++n) {
      char c;
      std::cin >> c;

      //std::cout << "read: " << c << " " << "before: ";
      //printchars(charlist);

      if (!charlist.empty()) {
        combinemap_t::iterator cit = combine_map.find(
            std::make_pair(charlist.back(), c));
        if (cit != combine_map.end()) {
          charlist.back() = cit->second;
        } else {
          charlist.push_back(c);
        }
      } else {
        charlist.push_back(c);
      }

      //std::cout << "middle: ";
      //printchars(charlist);

      elemset_t opposite_set;
      for (oppositemap_t::iterator it = opposite_map.begin(); it
          != opposite_map.end(); ++it) {
        if (it->second == charlist.back()) {
          opposite_set.insert(it->first);
          //std::cout << "opposite to " << c << " : " << it->first << "\n";
        }
      }

      for (charlist_t::iterator it = charlist.begin(); it != (--charlist.end()); ++it) {
        if (opposite_set.count(*it)) {
          charlist.clear();
          break;
        }

      }
      //std::cout << "after: ";
      //printchars(charlist);
    }

    std::cout << "Case #" << t + 1 << ": [";
    for (charlist_t::iterator it = charlist.begin(); it != charlist.end(); ++it) {
      std::cout << *it;
      if (it != --charlist.end())
        std::cout << ", ";
    }
    std::cout << "]\n";
  }

  return 0;
}
