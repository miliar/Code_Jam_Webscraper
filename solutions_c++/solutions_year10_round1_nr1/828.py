#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>
#include <vector>

//std::cin.ignore();

bool check(char c, const std::vector<std::string>& t, int K)
{
  int c1[50][50];
  int c2[50][50];
  int c3[50][50];
  int c4[50][50];
  memset(c1, 0, sizeof(c1));
  memset(c2, 0, sizeof(c2));
  memset(c3, 0, sizeof(c3));
  memset(c4, 0, sizeof(c4));
  int N = t.size();
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j < N; ++j) {
      //std::cout << i << "," << j << ":" << t[i][j] << std::endl;
      if(t[i][j] != c) {
        continue;
      } else {
        ++c1[i][j];
        ++c2[i][j];
        ++c3[i][j];
        ++c4[i][j];
      }      
      if(i > 0 && j > 0) {
        if(t[i-1][j-1] == c) {
          c1[i][j] += c1[i-1][j-1];
        }
      }
      if(i > 0 && j < N-1) {
        if(t[i-1][j+1] == c) {
          c2[i][j] += c2[i-1][j+1];
        }
      }
      if(i > 0) {
        if(t[i-1][j] == c) {
          c3[i][j] += c3[i-1][j];
        }
      }
      if(j > 0) {
        //std::cout << t[i][j-1] << "," << c << std::endl;
        if(t[i][j-1] == c) {
          c4[i][j] += c4[i][j-1];
        }
      }
      if(c1[i][j] == K || c2[i][j] == K || c3[i][j] == K || c4[i][j] == K) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    int N, K;
    std::cin >> N >> K;
    std::cin.ignore();
    std::vector<std::string> table;
    for(int i = 0; i < N; ++i) {
      std::string line;
      std::getline(std::cin, line);
      std::string::iterator it = std::remove(line.begin(), line.end(), '.');
      for(std::string::iterator x = it; x != line.end(); ++x) {
        *x = '.';
      }
      std::rotate(line.begin(), it, line.end());
      table.push_back(line);
      //std::cout << line << std::endl;
    }
    bool rwin = check('R', table, K);
    bool bwin = check('B', table, K);
    std::cout << "Case #" << t << ": ";
    if(rwin && bwin) {
      std::cout << "Both";
    } else if(rwin) {
      std::cout << "Red";
    } else if(bwin) {
      std::cout << "Blue";
    } else {
      std::cout << "Neither";
    }
    std::cout << std::endl;
  }
}
