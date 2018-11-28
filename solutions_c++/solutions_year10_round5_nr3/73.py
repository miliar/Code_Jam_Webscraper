#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

using namespace std;

typedef long long dbl;
typedef long long ll;
typedef pair <dbl, dbl> pnt;

int main( void )
{
  int tn;
  cin >> tn;

  for (int tt = 1; tt <= tn; tt++) {
    printf("Case #%d: ", tt);
    int n;
    cin >> n;
    map <int, int> v;
    for (int i = 0; i < n; i++) {
      int a, b;
      cin >> a >> b;
      v[a] += b;
    }
    int f = 1;
    int res = 0;
    while (f) {
      f = 0;
      forit (i, v) {
        if (i->second != 1) {
//          fprintf(stderr, "(%d;%d)\n", i->first, i->second);
          int x = i->first;
          v[i->first - 1]++;
          v[i->first + 1]++;
          v[i->first]-= 2;
          if (v[i->first] == 0) {
            v.erase(i);
          }
          f = 1;
          res++;
          break;
        }

      }
    }

    cout << res << endl;
  }

  return 0;
}

