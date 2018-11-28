#include <limits.h>
#include <cstring>
#include <cmath>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int C;
    std::cin >> C;
    std::vector<std::vector<char> > comb(26, std::vector<char>(26, '*'));
    for(int i = 0; i < C; ++i) {
      std::string l;
      std::cin >> l;
      comb[l[0]-'A'][l[1]-'A'] = l[2];
      comb[l[1]-'A'][l[0]-'A'] = l[2];
    }
    std::vector<std::vector<int> > opp(26, std::vector<int>(26));
    int D;
    std::cin >> D;
    for(int i = 0; i < D; ++i) {
      std::string l;
      std::cin >> l;
      opp[l[0]-'A'][l[1]-'A'] = 1;
      opp[l[1]-'A'][l[0]-'A'] = 1;
    }
    int N;
    std::cin >> N;
    std::string s;
    std::cin >> s;
    std::deque<char> q;
    std::vector<int> cnt(26);
    for(int i = 0; i < N; ++i) {
      if(q.empty()) {
        q.push_back(s[i]);
        ++cnt[q.back()-'A'];
      } else {
        char x = comb[q.back()-'A'][s[i]-'A'];
        if(x != '*') {
          --cnt[q.back()-'A'];
          q.pop_back();
          q.push_back(x);
          ++cnt[q.back()-'A'];
        } else {
          int j;
          for(j = 0; j < 26; ++j) {
            if(opp[s[i]-'A'][j] && cnt[j] > 0) {
              q.clear();
              cnt = std::vector<int>(26);
              break;
            }
          }
          if(j == 26) {
            q.push_back(s[i]);
            ++cnt[q.back()-'A'];
          }
        }
      }
    }
    std::cout << "Case #" << test << ": " << "[";
    std::string l;
    for(std::deque<char>::iterator i = q.begin(); i != q.end(); ++i) {
      l += *i;
      l += ", ";
    }
    std::cout << l.substr(0, l.size()-2) << "]" << std::endl;
  }
}
