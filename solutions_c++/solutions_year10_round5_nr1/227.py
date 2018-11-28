#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
using namespace std;
typedef pair<int,int> ii;
typedef long long ll;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

#define INPUT_NAME "A-small-0.in"
#define OUTPUT_NAME "A-small-0.out"

int K, D;
int P;
int max_seq;
ll seq[10];
bool used[10001];
bool isprime[10001];
VI primes;

void solve() {
	set<int> ans;
	if( K > 1 ) 
	for(int i=0;i<primes.size();++i) {
		if( primes[i] >= P ) break;
		if( max_seq >= primes[i] ) continue;
		ll MOD = primes[i];
		for(int A=0;A<MOD;++A) {
			ll x = seq[1];
			ll Ax = ( A * seq[0] ) % MOD;
			ll B = x - Ax;
			while( B < 0 ) B += MOD;
			B %= MOD;
			bool ok = true;
			for(int j=1;j<K;++j) {
				if( seq[j] != ( A * seq[j-1] + B ) % MOD ) {
					ok = false;
					break;
				}
			}
			if( ok ) {
				int s = (A * seq[K-1]+B) % MOD;
				ans.insert( s );
			}
		}
	}
	if( ans.size() != 1 ) {
		printf("I don't know.\n");
		fprintf(stderr,"I don't know.\n");
	}
	else {
		cout << *ans.begin() << endl;
		fprintf(stderr,"%d\n", *ans.begin());
	}
}

int main() {

	memset( isprime, 1, sizeof isprime );
	for(int i=4;i<=10000;i+=2) isprime[i] = false;
	primes.push_back(2);
	for(int i=3;i<=10000;i+=2) if( isprime[i] ) {
		primes.push_back(i);
		for(int j=i+i;j<=10000;j+=i) isprime[j] = false;
	}
	int tn;
	cin >> tn;
	FOR(cc,1,tn+1) {
		cin >> D >> K;
		max_seq = 0;
		REP(i,K) {
			cin >> seq[i];
			if( max_seq < seq[i] ) max_seq = seq[i];
		}
		P = 1;
		REP(i,D) P *= 10;
		fprintf(stderr,"Case #%d: ", cc);
		printf("Case #%d: ", cc);
		// output here!
		solve();
		
	}
	return 0;
}
