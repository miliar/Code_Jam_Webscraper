#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector <int > Vi;
typedef vector < Vi > Vii;
typedef long long LL;
typedef long long ll;
typedef vector < LL > Vll;
typedef vector < double > Vd;
typedef vector < string > Vs;
typedef pair<int,int> Pii;
typedef vector <Pii> Vpii;
typedef stringstream Iss;
typedef map<string,int> Msi;

#define Len 256
#define rep(i,n) for (int i=0; i<(n); ++i)
#define repd(i,n) for (int i((n)-1); i >= 0; --i)

#define For(var,p,k) for (int var=(p); var<=(k); ++var)
#define Ford(var,p,k) for (int var=(p); var>=(k); --var)
#define Foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define Foreachr(it, X) for(__typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(a,b) make_pair(a,b)
#define All(X)	(X).begin(),(X).end()
#define DBL_MAX numeric_limits<double>::max();

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void rmin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void rmax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }


static string infile, outfile;
static void init(int argc, char* argv[]){
    if (argc > 1)
    {infile = argv[1]; freopen(infile.c_str(),"r",stdin);}
    if (argc > 2)
    {outfile=argv[2];  freopen(outfile.c_str(),"w",stdout);}

}
template <typename T>
struct fun {
	bool operator()(const T& a, const T& b) const {
		return toupper(a) < toupper(b);
	}
};

int main(int argc, char* argv[]){
	init(argc,argv);
	int te;
	scanf("%d", &te);
	For (nr, 1, te){
		int nu = 0;
		int P,K,L;
		int keys[2000] = {0};
		Vi freq;
		cin >> P >> K >> L;
		rep(i,L){
			int n;
			cin >> n;
			freq.push_back(n);
		}
		sort(All(freq),greater<int>());
		int key = 0;
		ll count = 0;
		Foreach(it,freq){
			int ff = *it;
			if(keys[key] < P) {
				keys[key] ++;
				count += keys[key]*ff;
			}
			key ++;
			if (key >= K)
				key %= K;
		}

		printf("Case #%d: %I64d \n",nr,count);
	}
	return 0;

}

