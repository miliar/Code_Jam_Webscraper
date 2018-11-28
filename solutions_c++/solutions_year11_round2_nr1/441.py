using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin();  \
                           x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

const double EPS = 1e-9;
int cmp(double x, double y = 0, double tol = EPS){
  return( x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
double rpi(double wp, double owp, double oowp)
{
  return  0.25 * wp + 0.5 * owp + 0.25 * oowp;
}
vector<string> m;
vector<int> played;
vector<int> score;

void doit()
{
  vector<double> WP;
  vector<double> OWP;
  for (int i = 0; i < m.size(); ++i)
    {
      if(played[i] > 0)
        {
          WP.push_back((double)(score[i] * 1.0)/played[i]);
          double owp = 0;
          for(int j = 0; j < m[i].size() ; ++j)
            {
              if(m[i][j] != '.' and played[j] > 1)
                {
                  int p = played[j] - 1;
                  int s = score[j];
                  if(m[i][j] == '0')
                    s -= 1;
                  owp += (double)(s*1.0)/p;
                }
            }
          owp /= played[i];
          OWP.push_back(owp);
        }
      else
        {
          WP.push_back(0.0);
          OWP.push_back(0.0);
        }
    }
  for(int i = 0; i < WP.size() ; ++i)
    {
      if(played[i] > 0)
        {
          double oowp = 0;
          for(int j = 0; j < m[i].size() ; ++j)
            {
              if(m[i][j] != '.')
                oowp += OWP[j];
            }
          oowp /= played[i];
          cout << rpi(WP[i], OWP[i], oowp) << endl;
        }
      else
        puts("0");
    }
}
int main(){
  int casos;
  cin >> casos;
  for (int c = 1; c <= casos; ++c)
    {
      printf("Case #%d:\n", c);
      m.clear(), played.clear(), score.clear();
      string dummy;
      int N;
      cin >> N;
      for (int i = 0; i < N; ++i)
        {
          cin >> dummy;
          m.push_back(dummy);
          int s = 0, p = 0;
          for (int j = 0; j < dummy.size(); ++j)
            {
              if(dummy[j] == '1')
                s+=1;
              if(dummy[j] != '.')
                p+=1;
            }
          played.push_back(p);
          score.push_back(s);
        }
      doit();
    }
  return 0;
}
