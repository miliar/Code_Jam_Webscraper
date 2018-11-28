#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>


std::vector<std::pair<char, int> > moves;

int GetNextO(const int& k) {
  for (int i = k; i < moves.size(); ++i) {
    if (moves[i].first == 'O') {
      return moves[i].second;
    }
  }
  return 1;
}

int GetNextB(const int& k) {
  for (int i = k; i < moves.size(); ++i) {
    if (moves[i].first == 'B') {
      return moves[i].second;
    }
  }
  return 1;
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int n, t;
  
  std::cin >> t;
  for (int counter = 0; counter < t; ++counter) {
    std::cin >> n;
    moves.clear();
    for (int i = 0; i < n; ++i) {
      char c;
      int num;
      std::cin >> c >> num;
      moves.push_back(std::make_pair(c, num));
    }
    int o = 1, b = 1, no = GetNextO(0), nb = GetNextB(0);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (moves[i].first == 'O') {
        while (o != moves[i].second) {
          if (o < moves[i].second) {
            ++o;
          } else if (o > moves[i].second) {
            --o;
          }
          if (b < nb) {
            ++b;
          } else if (b > nb) {
            --b;
          }
          ++ans;
        } 
        ++ans;
        if (b < nb) {
          ++b;
        } else if (b > nb) {
          --b;
        }
        no = GetNextO(i+1);
      } else {
        while (b != moves[i].second) {
          if (b < moves[i].second) {
            ++b;
          } else if (b > moves[i].second) {
            --b;
          }
          if (o < no) {
            ++o;
          } else if (o > no) {
            --o;
          }
          ++ans;
        }
        if (o < no) {
          ++o;
        } else if (o > no) {
          --o;
        }
        ++ans;        
        nb = GetNextB(i+1);
      }
    }
    std::cout << "Case #" << counter+1 << ": " << ans << std::endl;
  }
  

  return 0;
}