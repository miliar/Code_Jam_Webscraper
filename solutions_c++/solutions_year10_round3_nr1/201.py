
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
#define forv(i, a) for(unsigned i=0; i<a.size(); i++)
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
  for (unsigned i = 0 ; i != s.size() ; i++ ) {
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

int main() {
  
  freopen("rope2.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int stest, N;
  int a[1003], b[1003];

  scanf("%d", &stest);

  rep(test, 1, stest) {

    scanf("%d", &N);
    fori(i, N) scanf("%d%d", &a[i], &b[i]);
    int res = 0;
    fori(i, N) fori(j, N) if(i < j && ((a[i] > a[j]) + (b[i] > b[j])) == 1)
      res ++;

    printf("Case #%d: %d\n", test, res);


  }
  fclose(stdin);
  fclose(stdout);
}
