/*****************************************************************************
 *************************** Macros and Typedefs *****************************
 *****************************************************************************/

// #pragma stacksize 1M twice
// #pragma comment(linked, "/STACK:16777216")

#include <algorithm>
#include <bitset>
#include <cassert>
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
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi(n) fo(i,n)
#define fj(n) fo(j,n)
#define fk(n) fo(k,n)
#define fl(n) fo(l,n)
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

typedef long long ll;
typedef long double ld;
typedef pair< int,int > ii;
typedef vector< int > vi;
typedef vector< double > vd;
typedef vector< ii > vii;
typedef vector< string > vs;
typedef vector< vi > vvi;
typedef vector< vd > vvd;

/*****************************************************************************
 ****************************** My Methods ***********************************
 *****************************************************************************/


// my stuff
const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
int bit_count(int x){ return x==0 ? 0 : 1+bit_count(x&(x-1)); }
inline int last_bit(int x){ return x&-x; } // 0011 0100 return 0000 0100

// math
inline int sign(double x){ return x<-EPS ? -1 : x>EPS ? 1 : 0; }
inline int sign(int x){ return (x>0)-(x<0); }
int nextComb(int x){            // x = xxx0 1111 0000
    int smallest = x&-x;        // 0000 0001 0000
    int ripple = x+smallest;    // xxx1 0000 0000
    int ones = x^ripple;        // 0001 1111 0000 // necessary to kill leading ones
    ones = (ones>>2)/smallest;  // 0000 0000 0111
    return ripple|ones;         // xxx1 0000 0111
}

// number theory
int gcd(int a, int b){ while(b){ int r=a%b; a=b; b=r; } return a; }
int lcm(int a, int b){ return a/gcd(a,b)*b; }

// UnionFind
struct UnionFind{

    vi P, S, R;
    UnionFind(int n): P(vi(n)), S(vi(n,1)), R(vi(n,1)){ fi(n) P[i]=i; }
    
    int findP(int x){
        if(P[x]!=x) P[x]=findP(P[x]);
        return P[x];
    }
    inline int operator[](const int x){ return findP(x); }
    
    int merge(int a, int b){
        int pa=findP(a), pb=findP(b);
        if(pa==pb) return 0;
        if(R[pa]<R[pb]){ P[pa]=pb; S[pb]+=S[pa]; }
        else{ P[pb]=pa; S[pa]+=S[pb]; }
        if(R[pa]==R[pb]) ++R[pa];
        return 1;
    }

};

/*****************************************************************************
 **************************** Scanner Methods ********************************
 *****************************************************************************/

const int BUF_SIZE = 1001*1000;
char buf[BUF_SIZE];

inline string getToken(){
    scanf("%s", buf);
    return buf;
}

inline string getLine(){
    fgets(buf, BUF_SIZE, stdin);
    return buf;
}

inline int getInt(){
    int a;
    scanf("%d", &a);
    return a;
}

inline ll getLL(){
	ll a;
	scanf("%lld", &a);
	return a;
}

inline double getDouble(){
    double a;
    scanf("%lf", &a);
    return a;
}

inline int stoi(string x){
    stringstream ss;
    int ret;
    ss << x;
    ss >> ret;
    return ret;
}

inline string itos(int x){
	stringstream ss;
	string ret;
	ss << x;
	ss >> ret;
	return ret;
}

inline vs split(string &s){
    stringstream ss; ss<<s; string t;
    vs ret;
    while(ss>>t) ret.pb(t);
    return ret;
}

template <class K, class V> 
vector<K> getKeys(map<K, V> m) {
    vector<K> keys;
    go(m, it)
        keys.pb(it->x); // the iterator goes thru key-value pairs
    return keys;
}

inline double myRand(){
    return ((double)rand()/RAND_MAX) + ((double)rand()/RAND_MAX/RAND_MAX);
}

/*****************************************************************************
 ************************* Problem Specific Code *****************************
 *****************************************************************************/

// END_CUT

void myCode(){
	int ttt = getInt();
	fo(tt,ttt) {
		int n = getInt(), s = getInt(), p = getInt();
		int ret = 0;
		fi(n) {
			int k = getInt();
			if (k > 3 * p - 3) ret++;
			else if (k > 3 * p - 5 && k > 1 && s) { ret++; s--; }
		}
		printf("Case #%d: %d\n",tt+1,ret);
	}
}

int main() {
  srand(time(NULL));
  myCode();
  return 0;
}
