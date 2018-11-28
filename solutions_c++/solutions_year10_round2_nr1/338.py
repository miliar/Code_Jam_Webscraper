#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <ios>
#include <istream>
#include <ostream>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <bitset>
#include <map>

#include <new>
#include <functional>
#include <string>
#include <iterator>
#include <algorithm>
#include <complex>
#include <utility>
#include <numeric>
#include <typeinfo>

using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))
#define sqr(x) ((x) * (x))
#define SZ(x) (int(x.size()))

#define TIMER_A(timer) int timer = clock()
#define TIMER_B(timer) cerr << (#timer) << ": " << (double)(clock() - timer) / CLOCKS_PER_SEC << endl

#define debug(x) cerr << (#x) << ": " << (x) << endl
#define debug_array(x, N) \
cout << (#x) << ":"; \
for (int i = 0; i < N; ++i) \
  cout << " " << x[i]; \
cout << endl
#define echo(x) cerr << (#x) << endl

#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const double eps = 1e-8;
const double pi = acos(-1.0);
const int oo = 0x7f7f7f7f;

typedef long long LL;

struct Dir
{
  static int cnt;

  map<string, Dir> sub;
  
  void insert (const string &path, int dx)
  {
    int t = dx + 1;
    int n = path.size();
    while (t < n && path[t] != '/')
      ++t;
    string dir = path.substr(dx, t - dx);
    if (sub.find(dir) == sub.end())
    {
      ++cnt;
      sub.insert(MP(dir, Dir()));
    }
    if (t < n)
      sub[dir].insert(path, t);
  }
  
  void free ()
  {
    for (map<string, Dir>::iterator i = sub.begin(); i != sub.end(); ++i)
      i->SE.free();
    sub.clear();
  }
};

int Dir::cnt = 0;

int TC, TN;
int N, M;

Dir root;

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d%d ", &N, &M);
    root.free();
    string path;
    for (int i = 0; i < N; ++i)
    {
      getline(cin, path);
      if (!isalnum(path[path.size() - 1]))
        path = path.substr(0, path.size() - 1);
      root.insert(path, 0);
    }
    int n1 = Dir::cnt;
    for (int i = 0; i < M; ++i)
    {
      getline(cin, path);
      if (!isalnum(path[path.size() - 1]))
        path = path.substr(0, path.size() - 1);
      root.insert(path, 0);
    }
    int n2 = Dir::cnt;
    printf("Case #%d: %d\n", TC, n2 - n1);
  }
}
