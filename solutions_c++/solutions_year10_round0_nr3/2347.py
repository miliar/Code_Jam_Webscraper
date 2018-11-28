#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define fori(i,n) for(int i=0; i<n; i++)
#define rep(i, a, b) for(int i=a;i<=b;i++)
#define forv(i, a) for(int i=0; i<a.size(); i++)
typedef long long int64;
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(
vector<string> split( const string& s, const string& delim =" " ) {
  vector<string> res;
  string t;
  for ( unsigned i = 0 ; i != s.size() ; i++ ) {
    if ( delim.find( s[i] ) != string::npos ) {
      if ( !t.empty() ) {
        res.push_back( t );
        t = "";
      }
    } else {
      t += s[i];
    }
  }
  if ( !t.empty() ) {
    res.push_back(t);
  }
  return res;
}

int stest, n, R, K;
int g[1003];
int flag[1003];
int64 amount[1003];
int64 res;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &stest);
  for(int e=1; e<=stest; e++) {
    scanf("%d%d%d", &R, &K, &n);
    fori(i, n) scanf("%d", &g[i]);

    res = 0;
    memset(flag, -1, sizeof(flag));
    int nh = 0;
    for(int step=0; step < R; step++) {
      int64 cur = 0;

      if (flag[nh] != -1) {
        int sl = step - flag[nh];
        int64 m = (R-step)/sl;
        res += m*(res-amount[nh]);
        step += sl*m;
        //cout << step << " " << sl << " " << m << endl;
        while(step < R) {
          int64 cur = 0;
          int initnh = nh;
          while(cur < K) {
            if(cur + g[nh] <= K) {
              cur += g[nh++];
              nh%=n;
            } else break;
            if (nh == initnh) break;
          }
          res += cur;
          step++;
        }
        continue;
      }


      flag[nh] = step;
      amount[nh] = res;
      int initnh = nh;
      while(cur < K) {
        if(cur + g[nh] <= K) {
          cur += g[nh++];
          nh%=n;
        } else break;
        if (nh == initnh) break;
      }
      res += cur;
    }
    printf("Case #%d: %lld\n", e, res);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
