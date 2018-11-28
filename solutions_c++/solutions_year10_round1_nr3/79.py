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
#include <string.h>
#include <gmp.h>
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

long long  binarySearch(long long  low, long long high, bool (* _target) (long long t1)){ 
   while(low < high){ long long mid = low + (high - low) / 2; if(_target(mid)) high = mid; else low = mid+1;} return low;
}

long long gcd(long long A, long long B){  
   if(!A && !B) return 0;  
   return (A%B)?gcd(B,A%B):B; 
}

int _T;
int A1, A2, B1, B2;

bool winstate(int a, int b){
  if(a < b) swap(a,b);
  if(a > 1000000) return true; if(a == b) return false; if(a%b==0) return true;
  if(a < 2*b) return !winstate(b,a-b);
  return !winstate(b,a%b) || !winstate(a%b+b,b);
}

int start;
int dp[1000005];

bool canwin(long long A){ return winstate(A,start); }

int main(){
  cin >> _T;
/*
  FOR(i,1,1000001){
	start = i; dp[i] = binarySearch(i+1,1000004,canwin);
        if(i%10000 == 0) cerr << i << endl;
	cout << dp[i] << endl;
  }
*/
  ifstream in("C-vals.dat");
  int pos = 1; while(in >> dp[pos]) pos++;
  in.close();

  FOR(i,0,_T){
    cout << "Case #" << (i+1) << ": ";
    cin >> A1 >> A2 >> B1 >> B2;
    long long ret = 0;
    FOR(a,A1,A2+1) if(B1 >= dp[a]) ret += (B2-B1+1); else if(B2 >= dp[a]) ret += (B2-dp[a]+1);
    FOR(b,B1,B2+1) if(A1 >= dp[b]) ret += (A2-A1+1); else if(A2 >= dp[b]) ret += (A2-dp[b]+1);
    cout << ret;
    cout << endl;
  }
  return 0;
}

