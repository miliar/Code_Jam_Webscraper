#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
static const int INF = std::numeric_limits<int>::max();
int main()
{
  std::vector<char> tr(26);
  tr[0] = 24;
  tr[1] = 7;
  tr[2] = 4;
  tr[3] = 18;
  tr[4] = 14;
  tr[5] = 2;
  tr[6] = 21;
  tr[7] = 23;
  tr[8] = 3;
  tr[9] = 20;
  tr[10] = 8;
  tr[11] = 6;
  tr[12] = 11;
  tr[13] = 1;
  tr[14] = 10;
  tr[15] = 17;
  tr[16] = 25;
  tr[17] = 19;
  tr[18] = 13;
  tr[19] = 22;
  tr[20] = 9;
  tr[21] = 15;
  tr[22] = 5;
  tr[23] = 12;
  tr[24] = 0;
  tr[25] = 16;
  int T;
  std::cin >> T;
  std::cin.ignore();
  for(int test = 1; test <= T; ++test) {
    std::string line;
    std::getline(std::cin, line);
    for(int i = 0; i < (int)line.size(); ++i) {
      if(line[i] != ' ') {
        line[i] = tr[line[i]-'a']+'a';
      }
    }
    std::cout << "Case #" << test << ": " << line << std::endl;
  }
}
