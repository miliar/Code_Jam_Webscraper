/*****************************************************************************
 *************************** Macros and Typedefs *****************************
 *****************************************************************************/

// #pragma stacksize 1M twice
// #pragma comment(linked, "/STACK:16777216")

#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <time.h>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi(n) fo(i,n)
#define fj(n) fo(j,n)
#define fk(n) fo(k,n)
#define fd(i,n) for(int i=(int)(n)-1; i>=0; --i)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)a; i<(int)b; ++i)
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define srt(x) sort(all(x))
#define go(x,it) for(typeof((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define PQ(t) priority_queue< t, vector<t>, greater<t> >
#define x first
#define y second
#define me (*this)
#define CLR(a,v) memset(a, v, sizeof(a))
#define UNIQUE(a) srt(a); a.resize(unique(all(a))-a.begin())
#define RAND (((double)rand()/RAND_MAX) + ((double)rand()/RAND_MAX/RAND_MAX))

typedef long long ll;
typedef long double ld;

typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector< vii > vvii;

typedef vector< int > vi;
typedef vector< vi > vvi;

typedef vector< double > vd;
typedef vector< vd > vvd;

typedef vector< ll > vll;
typedef vector< vll > vvll;

typedef vector< string > vs;

/*****************************************************************************
 ****************************** My Methods ***********************************
 *****************************************************************************/

// my stuff
const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
int bit_count(int x){ return x==0 ? 0 : 1+bit_count(x&(x-1)); }
inline int low_bit(int x){ return x&-x; } // 0011 0100 return 0000 0100
inline int sign(double x){ return x<-EPS ? -1 : x>EPS ? 1 : 0; }
inline int sign(int x){ return (x>0)-(x<0); }
template<class T> void chmin(T &t, T f){ if(t > f) t = f; }
template<class T> void chmax(T &t, T f){ if(t < f) t = f; }

/*****************************************************************************
 **************************** Scanner Methods ********************************
 *****************************************************************************/

inline int getint(){
  int a;
  return scanf("%d", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}

inline double getdouble(){
  double a;
  return scanf("%lf", &a) ? a : (fprintf(stderr, "trying to read\n"),-1.0);
}


/*
 *  // does not get the new line
 *  getline(cin, s);
 *
 *  struct comp_1{
 *      bool operator()(const ii &a, const ii &b) const{
 *          return a.x!=b.x ? a.x<b.x : a.y<b.y;
 *      }
 *  };
 *
 *  sprintf(buf, "%s%d%s%d%s\n", "Hell", 0, " W", 0, "rld!");
 *
 *  (map<int,int>::iterator it = cache.begin(); it!=cache.end(); ++it)
 */

/*
const int BUF_SIZE = 1001*1000;
char buf[BUF_SIZE];

inline string gettoken(){
    return scanf("%s", buf) ? buf : (fprintf(stderr, "trying to read\n"),"");
}

// does not return the new line
inline string getline(){
    string ret;
    getline(cin, ret);
    // getline(cin, ret, ':'); // to use ':' as the delimiter
    return ret;
}
*/

/*****************************************************************************
 ************************* Problem Specific Code *****************************
 *****************************************************************************/

// END_CUT

int closest(ll x1, ll x2, ll x3, int y1, int y2, int y3){
  return (x3-x2)*(y2-y1) >= (y3-y2)*(x2-x1);
}

void myCode(){
  int ttt=getint();
  fo(tt,ttt){
    int n=getint();
    vi a(n-1);
    fi(n-1)
      a[i]=getint()-1;

    int boned = 0;
    fi(n-1)
      fr(j,i+1,a[i])
        if(a[j] > a[i])
          boned = 1;

    printf("Case #%d:", tt+1);

    if(boned){
      printf(" Impossible\n");
      continue;
    }

    vll b(n);
    bool done = false;
    while(!done){
      fi(n)
        b[i] = (ll)(RAND*((1e9)-1));
      int ok = 1;
      fi(n-1){
        fr(j,i+1,a[i])
          if(closest(i, j, a[i], b[i], b[j], b[a[i]]))
            ok = 0;
        fr(j,a[i],n)
          if(!closest(i, a[i], j, b[i], b[a[i]], b[j]))
            ok = 0;
      }
      if(ok)
        done = true;
    }

    fi(n)
      printf(" %lld", b[i]);
    printf("\n");

  }
}

int main() {
  srand(time(NULL));
  myCode();
  return 0;
}
