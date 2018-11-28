#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
#include <strings.h>

using namespace std;

static inline int round_power_of_two(int x)
{
  x--;
  x |= x >> 1;
  x |= x >> 2;
  x |= x >> 4;
  x |= x >> 8;
  x |= x >> 16;
  x++;
  return x;
}

static inline int highest_set_bit(int x)
{
  return ffs(round_power_of_two(x)) - 1;
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    vector<int> C;
    int N;
    cin >> N;
    for(int i = 0; i < N; i++)
    {
      int Ci;
      cin >> Ci;
      C.push_back(Ci);
    }

    sort(C.rbegin(), C.rend());

    int r = 0;
    int s = 0;
    for(size_t i = 0; i < C.size(); i++)
    {
      r ^= C.at(i);
      if(i != C.size() - 1)
      {
        s += C.at(i);
      }
    }
    if(r != 0)
    {
      cout << "Case #" << t << ": NO" << endl;
    }
    else
    {
      cout << "Case #" << t << ": " << s << endl;
    }
  }
}

