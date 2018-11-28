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

void search(std::vector<std::pair<int, int> >& res,
            std::vector<std::string> table,
            int m, int n)
{
  int qsize = std::min(m, n);
  int count = 0;
  while(qsize) {
    //std::cout << "qsize=" << qsize << std::endl;
    for(int i = 0; i < m; ++i) {
      if(m-i < qsize) break;
      for(int j = 0; j < n; ++j) {
        if(n-j < qsize) break;
        if(table[i][j] == '.') { continue; }
        char nc = table[i][j];
        //std::cout << "from " << i << "," << j << std::endl;
        for(int ki = 0; ki < qsize; ++ki) {
          for(int kj = 0; kj < qsize; ++kj) {
            //std::cout << " " << i+ki << "," << j+kj << std::endl;
            if(table[i+ki][j+kj] != nc) {
              goto NEXT;
            }
            nc = table[i+ki][j+kj] == 'B'?'W':'B';
          }
          if(qsize%2 == 0) {
            nc = nc == 'B'?'W':'B';
          }
        }
        for(int ki = 0; ki < qsize; ++ki) {
          for(int kj = 0; kj < qsize; ++kj) {
            table[i+ki][j+kj] = '.';
          }
        }
        ++count;
      NEXT:
        ;
      }
    }
    if(count) {
      //std::cout << qsize << ":" << count << std::endl;
      res.push_back(std::make_pair(qsize, count));
    }
    --qsize;
    count = 0;
  }
}

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    std::vector<std::string> table;
    int M, N;
    std::cin >> M >> N;
    std::cin.ignore();
    for(int j = 0; j < M; ++j) {
      std::string line;
      std::getline(std::cin, line);
      std::string x;
      for(size_t i = 0; i < line.size(); ++i) {
        unsigned char c = line[i];
        if(c >= 'A') {
          c -= 'A';
          c += 10;
        } else {
          c -= '0';
        }
        for(int j = 0; j < 4; ++j) {
          if(c&(1 << (3-j))) {
            x += 'B';
          } else {
            x += 'W';
          }
        }
      }
      table.push_back(x);
    }
    std::vector<std::pair<int, int> > res;
    search(res, table, M, N);
    std::cout << "Case #" << t << ": " << res.size() << std::endl;
    for(size_t i = 0; i < res.size(); ++i) {
      std::cout << res[i].first << " " << res[i].second << std::endl;
    }
  }
}
