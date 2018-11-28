#include <string>
#include <iostream>
#include <sstream>
#include <map>
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

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LINF 90000000000000000000LL
#define LLMAX ((unsigned long long)(-1))

//BEGIN CUT - BitStuff
int numBits(unsigned long long v) {return __builtin_popcount(v>>32) + __builtin_popcount(v & ((SHIFT(32)-1)));}
int highestBit(unsigned long long v) { return (v==0)?-1:(((v>>32)!=0)?63-__builtin_clz(v>>32):31-__builtin_clz(v));}
int lowestBit(unsigned long long v) { return (v==0)?-1:((((v>>32)<<32)==v)?32 + __builtin_ctz(v>>32):__builtin_ctz(v));}
inline void flip(long long &m, int v) { m ^= SHIFT(v);}

inline void flip(int &m, int v) { assert(v<32); m ^= SHIFT(v);}
bitset<8> toBinary(char c) { return bitset<8>(c);}
bitset<32> toBinary(int n) { return bitset<32>(n);}
bitset<64> toBinary(long long n){ return bitset<64>(bitset<64>(n) | (bitset<64>(n>>32)<<32));}
//END CUT - BitStuff

int dp[80][80][SHIFT(12)];
string grid[80];
int rows, cols;

bool okay(int i){
   int cnt = 0;
   bool last = false;
   while(i>0){
     if((i&1)&& (last||grid[0][cnt]=='x')) return false;
     if(i&1) last = true; else last = false;
     cnt++; i>>=1;
   }
   return true;
}

int getmask(int r, int c, int mask){
   int ret = 0;
   if(c!=0) ret |= mask & SHIFT(0);
   if(c!=0) ret |= mask & SHIFT(cols);
   if(c!=cols-1) ret |= mask & SHIFT(2);
   return ret;
}

int solve(int r, int c, int mask){
    if(c==cols) c = 0, r++;
    if(r==rows) return 0;
    if(dp[r][c][mask]!=-1) return dp[r][c][mask];
    
    int rmask = getmask(r,c,mask);

//    cout << "Solve: " << r << " " << c << " " << toBinary(mask) << " (" << rmask << ") " << endl;

    dp[r][c][mask] = solve(r,c+1,mask>>1);
    if(grid[r][c]!='x' && rmask==0) dp[r][c][mask] = max(dp[r][c][mask], 1 + solve(r,c+1,mask>>1 | SHIFT(cols))); 

//    cout << "Solved: " << r << " " << c << " " << toBinary(mask) << " -> " << dp[r][c][mask] << endl;
    return dp[r][c][mask];
}

int _times;
int main(){
  cin >> _times;
  FOR(_t,1,_times+1){
    MEMSET(dp,-1);
    cin >> rows >> cols;
    FOR(i,0,rows) cin >> grid[i];

    int ret = 0;
    FOR(i,0,SHIFT(cols)) if(okay(i)){
  //       cout << " " << i << " " << numBits(i) << " " << ret <<endl;
	 ret = max(ret,solve(1,0,i<<1) + numBits(i));
//         cout << " " << i << " " << numBits(i) << " " << solve(1,0,i<<1) << " -> " << ret << endl;
    }
    cout << "Case #" << _t << ": " << ret << endl;
//    break;
  }
  return 0;
}
