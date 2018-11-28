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

ll dp[1<<21];

void myCode(){
  int ttt=getint();
  fo(tt,ttt){

    ll money; cin >> money;
    ll fee=getint();
    int n=getint();
    vector< pair< ll,ll > > aa;
    fi(n){
      // price, stale
      ll x, y;
      cin >> x >> y;
      aa.pb(mp(x,y));
    }
    srt(aa);
    aa.resize(unique(all(aa))-aa.begin());
    n=sz(aa);

    vector< pair< ll,ll > > a;
    fi(n){
      // must be cheaper than guy after, and more stale than guy before
      // if there is someone behind me, I have to beat him on price, cuz if we have
      // the same price, he is beating me on stale
      if((i==n-1 || aa[i].x < aa[i+1].x) && (i==0 || a.empty() || aa[i].y > a.back().y))
        a.pb(aa[i]);
    }
    n = sz(a);

    vector< pair< ll,ll > > b; // time it lasts, price
    b.pb(mp((ll)a[0].y+1, (ll)(a[0].y+1)*a[0].x+fee));
    fr(i,1,n)
      b.pb(mp(a[i].y+1, b.back().y+(ll)(a[i].y-a[i-1].y)*a[i].x));

    // for small test case, n*m knapsack
    fi(1<<21)
      dp[i] = INF;
    dp[0] = 0;
    fr(i,1,1<<21)
      fj(n)
        if(i-b[j].x < 0){
          if(j==0){
            chmin(dp[i], i*a[j].x+fee);
          }else{
            chmin(dp[i], b[j-1].y + (i-b[j-1].x)*a[j].x);
          }
          break; // don't do negative shit
        }else{
          chmin(dp[i], b[j].y+dp[i-b[j].x]);
        }

    int lo=0, hi=1<<21;
    while(hi-lo > 1){
      int mid = (hi+lo)/2;
      if(dp[mid] > money)
        hi = mid;
      else
        lo = mid;
    }

    printf("Case #%d: %d\n", tt+1, lo);

  }
}

int main() {
  srand(time(NULL));
  myCode();
  return 0;
}
