#include <cassert>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <iterator>
#include <set>
#include <map>
#include <vector>

//std::cin.ignore();

class Shorter {
public:
  bool operator()(const std::string& lhs, const std::string& rhs) const
  {
    int ln = std::count(lhs.begin(), lhs.end(), '/');
    int rn = std::count(rhs.begin(), rhs.end(), '/');
    if(ln == rn) {
      return lhs < rhs;
    } else {
      return ln-rn;
    }
  }
};

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int N, M;
    std::cin >> N >> M;
    std::cin.ignore();
    std::set<std::string> dirs;
    for(int i = 0; i < N; ++i) {
      std::string line;
      std::getline(std::cin, line);
      line += "/";
      for(size_t j = 1; j < line.size(); ++j) {
        if(line[j] == '/') {
          std::string subpath = line.substr(0, j+1);
          dirs.insert(subpath);
        }
      }
    }
    std::vector<std::string> s;
    for(int i = 0; i < M; ++i) {
      std::string line;
      std::getline(std::cin, line);
      if(line == "/") continue;
      line += "/";
      s.push_back(line);
    }
    int count = 0;
    std::sort(s.begin(), s.end(), Shorter());
    for(int i = 0; i < M; ++i) {
      std::string d = s[i];
      for(size_t j = 1; j < d.size(); ++j) {
        if(d[j] == '/') {
          std::string subpath = d.substr(0, j+1);
          if(dirs.count(subpath) == 0) {
            ++count;
            dirs.insert(subpath);
          }
        }
      }
    }
    std::cout << "Case #" << t << ": " << count << std::endl;
  }
}
