#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <map>
#include <complex>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(long long a=(long long)(b);a<(long long)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define SUBSET(a,b) for(long long a = b; a!=0; a = (b & (a-1)))
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<long long,long long>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LLINF ((1LL<<62)-1)


// ---------------------------------------------------------------------------------
//BEGIN CUT - Print Array - O(N)
void printArray(const vector<string> & v) { FOR(i,0,v.size()) cout << v[i] << endl; cout << endl; }
template<class T> 
void printArray(const vector<T> & v) { FOR(i,0,v.size()) cout << v[i] << " "; cout << endl; }
template <class T>
void printArray(const vector<vector<T> > &v){ FOR(i,0,v.size()) printArray(v[i]);}
//END CUT - Print Array

//BEGIN CUT - Graph deltas
int dr4[] = {0,0,-1,1},           dc4[] = {1,-1,0,0};
int dr8[] = {0,0,1,1,1,-1,-1,-1}, dc8[] = {1,-1,-1,0,1,-1,0,1};
//END CUT - Graph deltas

// BEGIN CUT - Misc. Data
string months[] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
string daysOfWeek[] = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
int daysOfMonth[] = {31,28,31,30,31,30,31,31,30,31,30,31};

string lettersU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string lettersL = "abcdefghijklmnopqrstuvwxyz";
// BEGIN CUT - Misc. Data

//BEGIN CUT - HexStuff [ USED BY Bigint ]
string _hexdigits = "0123456789ABCDEF";
unsigned long long toHexLong(string str){ unsigned long long num = 0; FOR(i,0,str.length()) { num<<=4; if(isalpha(str[i])) num += (str[i]-'A'+10); else num += (str[i]-'0');} return num; }
string toHexString(unsigned long long num) {string ret; FOR(k,0,16) { ret += _hexdigits[((num>>(k<<2))&0xF)]; } reverse(ret.begin(),ret.end()); return ret;}
//END CUT - HexStuff

//BEGIN CUT - Math Functions - O(digits^2) [ USED By Bigint, Choose, Frac]
long long gcd(long long A, long long B){  if(!A && !B) return 0;  return (A%B)?gcd(B,A%B):B; }
long long lcm(long long A, long long B){ if(!A && !B) return 0; return A / gcd(A,B) * B; }
long long gcdext(long long A, long long B, long long &Aout, long long &Bout, long long cmod){ long long r,t; if(A%B==0) { Aout = 0, Bout = 1; r = B; } else{ r = gcdext(B,A%B,Aout,Bout,cmod); t = Bout; Bout = (Aout - A/B * Bout) % cmod; Aout = t;} return r;}
long long ModDiv(long long num, long long denom, long long mod){ long long A, B; gcdext(mod,denom,A,B,mod); return ((num * B) % mod + mod) % mod;}
//END CUT - Math Functions

//BEGIN CUT - Random Functions [ USED BY Bigint]
static bool _seeded = false;
unsigned long long lrand(int seed=-1){ if(!_seeded) _seeded=true,srand((seed==-1)?time(0):seed); return ((((unsigned long long)rand())<<32) | rand());}
//END CUT - Random Functions
// ---------------------------------------------------------------------------------

int _T;
long long N;
vector<long long> T;

int main(){
  cin >> _T;
  FOR(i,0,_T){
    cout << "Case #" << (i+1) << ": ";
    cin >> N; T.resize(N);
    FOR(j,0,N) cin >> T[j];
    sort(BEGEND(T));
    FOR(j,1,N) T[j]-=T[0];
    long long g = T[1]; FOR(i,2,N) g = gcd(g,T[i]);
    if(g >= T[0]) cout << g-T[0];
    else if(T[0]%g==0) cout << 0;
    else cout << (1+T[0]/g)*g-T[0];

    cout << endl;
  }
  return 0;
}

