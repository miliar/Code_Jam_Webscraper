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
void print(const string & s, int c)
{
  printf("Case #%d: [", c);
  int n = s.size();
  for(int i = 0; i < n -1; ++i)
    printf("%c, ", s[i]);
  if(s.size())
    printf("%c", s[s.size()-1]);
  puts("]");
}


int main(){
  int t;
  cin >> t;
  for(int w = 1; w <= t; ++w)
    {
      int c;
      cin >> c;
      map<string, string> combine;
      string dummy;
      while(c-- and cin >> dummy)
        {
          string key1 = "", key2 = "", val = "";
          key1 += dummy[0], key1 += dummy[1];
          key2 += dummy[1], key2 += dummy[0];
          val += dummy[2];
          combine[key1] = val;
          combine[key2] = val;
        }
      int d;
      cin >> d;
      map<string, set<string> > opposed;
      while(d-- and cin >> dummy)
        {
          string key1 = "", key2 = "";
          key1 += dummy[0], key2 += dummy[1];
          opposed[key1].insert(key2);
          opposed[key2].insert(key1);
        }
      int n;
      string invocation;
      cin >> n >> invocation;
      string ans = "";
      for(int i = 0 ; i < n ; ++i)
        {
          ans += invocation[i];

          int m = ans.size();
          if(m >= 2)
            {
              string key = "";
              key += ans[m-2], key += ans[m-1];
              string val = combine[key];
              if(val.size() > 0)
                {
                  string temp = "";
                  for(int j = 0; j < m - 2 ; ++j)
                    {
                      temp+=ans[j];
                    }
                  temp+=val;
                  ans = temp;
                }
              string last = "";
              last += ans[ans.size()-1];
              for(int j = 0; j < ans.size()-1 ; ++j)
                {
                  string temp = "";
                  temp += ans[j];
                  if(opposed[last].count(temp))
                    {
                      ans = "";
                      break;
                    }
                }
            }          
        }
      print(ans,w);
    }
  return 0;
}
