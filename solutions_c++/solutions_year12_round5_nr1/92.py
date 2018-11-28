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

struct comp_1{
  bool operator()(const pair< ii,int > &a, const pair< ii,int > &b){
    return b.x.y*a.x.x < a.x.y*b.x.x || (b.x.y*a.x.x == a.x.y*b.x.x && a.y < b.y);
/*
    bool ret = a.x.x*(100-b.x.y) < b.x.x*(100-a.x.y) || (a.x.x*(100-b.x.y) == b.x.x*(100-a.x.y) && a.y < b.y);
    fprintf(stderr, "%d %d\n", a.x.x*(100-b.x.y), b.x.x*(100-a.x.y));
    fprintf(stderr, "a=(%d,%d), b=(%d,%d), ret=%d\n", a.x.x, a.x.y, b.x.x, b.x.y, ret?1:0);
    return ret;
*/
  }
};

void myCode(){
  int ttt=getint();
  fo(tt,ttt){
    int n=getint();
    vi t;
    fi(n)
      t.pb(getint());
    vi p;
    fi(n)
      p.pb(getint());

    vector< pair< ii,int > > a;
    fi(n)
      a.pb(mp(ii(t[i],p[i]),i));
    sort(all(a), comp_1());
/*
    fi(n)
      fprintf(stderr, "(%d,%d) ", a[i].x.x, a[i].x.y);
    fprintf(stderr, "\n");
*/
    printf("Case #%d:", tt+1);
    fi(n)
      printf(" %d", a[i].y);
    printf("\n");

  }
}

int main() {
  srand(time(NULL));
  myCode();
  return 0;
}
