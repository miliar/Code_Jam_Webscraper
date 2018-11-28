// Paste me into the FileEdit configuration dialog

#include <cmath>
#include <ctime>
#include <iostream>
#include <string>

#include <vector>
#include <map>
#include <utility>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <sstream>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
typedef long long int LL;

template<class T1,class T2> T2 parse(T1& s) { stringstream i; i << s; T2 x; i>>x; return x; }
int s2i(string s) { return parse<string,int>(s); }
string i2s(int s) { return parse<int,string>(s); }
#define debug(x) cerr << #x << " = " << x << "\n";

int
main(void)
{
  int C;
  scanf("%d", &C);
  for (int c = 0; c < C; c++)
    {
      int R;
      set< pair<int, int> > p;
      scanf("%d", &R);
      fprintf(stderr, "%d\n", c);
      for (int r = 0; r < R; r++)
        {
          int x1, x2, y1, y2;
          scanf("%d", &x1);
          scanf("%d", &y1);
          scanf("%d", &x2);
          scanf("%d", &y2);
          for (int x = x1; x <= x2; x++)
            for (int y = y1; y <= y2; y++)
              {
                p.insert(make_pair(x, y));
              }
        }
      int sec = 0;
      while (true)
        {
          if (sec % 20 == 0)
            fprintf(stderr, "  %d\n", sec);
          set< pair<int, int> > np;
          if (p.empty()) break;
          sec ++;
          set< pair<int, int> >::iterator i;
          for (i = p.begin(); i != p.end(); ++i)
            {
              pair<int, int> copp = *i;
              bool w = p.find(make_pair(copp.first-1, copp.second)) != p.end();
              bool n = p.find(make_pair(copp.first, copp.second-1)) != p.end();
              if (n || w)
                {
                  np.insert(make_pair(copp.first, copp.second));
                }
              w = p.find(make_pair(copp.first+1, copp.second-1)) != p.end();
              n = p.find(make_pair(copp.first-1, copp.second+1)) != p.end();
              if (n)
                {
                  np.insert(make_pair(copp.first, copp.second+1));
                }
              if (w)
                {
                  np.insert(make_pair(copp.first+1, copp.second));
                }

            }
          p = np;
        }
      printf("Case #%d: %d\n", c+1, sec);
    }

  return 0;
}
