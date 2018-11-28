#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <ios>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <utility>
#include <numeric>
#include <algorithm>

#define PRT(x) #x << ' ' << (x) << ' '
#define LNG(x) (sizeof(x)/sizeof(*(x)))

using namespace std;

#define ALPHANUM 'z' - 'a' + 1
#define toIndex(c) ((c) - 'a')
#define toChar(x) (char)((x) + 'a')

const char * from[] =
{
  "y qee",
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv",
};

const char * to[] =
{
  "a zoo",
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up",
};

#define MAX_G 128

int T;
char G[MAX_G];
char map[ALPHANUM];

void definetable()
{
  memset(map, 0, sizeof(map));
  for(size_t i=0; i < sizeof(from)/sizeof(from[0]); ++i)
  {
    ;
    for(const char *x=from[i], *y=to[i], *p=x, *q=y;
        *p != '\0' && *q != '\0'; ++p, ++q)
    {
      if(*p == ' ') { continue; }
      if(0 == map[toIndex(*p)]) {
        map[toIndex(*p)] = *q;
      }
      assert(*q == map[toIndex(*p)]);
    }
  }
  bool exists[ALPHANUM] = {false};
  size_t undefined_key = 0;
  bool undefined_key_found = false;
  for(size_t i=0; i<ALPHANUM; ++i)
  {
    if(map[i] == 0) {
      cerr << toChar(i) << " mapping not found\n";
      if(undefined_key_found)
      {
        assert(map[i] != 0);
      }
      undefined_key_found = true;
      undefined_key = i;
    }
    else {
      exists[toIndex(map[i])] = true;
    }
  }
  for(size_t i=0; i<ALPHANUM; ++i)
  {
    if(!exists[i] && undefined_key_found)
    {
      cerr << "Assume "
           << toChar(undefined_key) << " -> "
           << toChar(i) << "\n";
      map[undefined_key] = toChar(i);
    }
  }
}

void solve()
{
  for(size_t i=0; G[i] != '\0' && i<MAX_G; ++i)
  {
    if(G[i] != ' ') { G[i] = map[toIndex(G[i])]; }
  }
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);

  definetable();

  memset(G, 0, sizeof(G));

  cin >> T;
  cin.getline(G, MAX_G);
  for(int X=1; X<=T; ++X)
  {
    cin.getline(G, MAX_G);
    solve();
    cout << "Case #" << X << ": " << G << endl;
  }
  return 0;
}
