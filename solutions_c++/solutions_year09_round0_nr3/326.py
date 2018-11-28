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
#define SUBSET(a,b) for(long long a = 0; a!=0; a = (b & (a-1)))
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<long long,long long>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)



string wtcj = "welcome to code jam", dummy, line;
const int mod = 10000;
int dp[30][500];


void padout(int num){
   if(num < 10) cout << "000";
   else if(num < 100) cout << "00";
   else if(num < 1000) cout << "0";
   cout << num;
}

int solve(int wpos, int cpos){
   if(wpos == wtcj.length()) return 1; 
   else if(cpos == line.length()) return 0;
   //cout << wpos << " " << cpos << endl;
   int &ret = dp[wpos][cpos]; if(ret!=-1) return ret; ret = solve(wpos,cpos+1);
   if(wtcj[wpos] == line[cpos]) ret = (ret + solve(wpos+1,cpos+1)) % mod;
   //cout << wpos << " " << cpos << " ->" << ret << endl;
   return ret;
}

int _T;
int main(){
  cin >> _T; getline(cin,dummy);
//  cout << "DUMMY: " << dummy << endl;
  FOR(i,0,_T){
    cout << "Case #" << (i+1) << ": ";
    getline(cin,line); MEMSET(dp,-1);
  //  cout << "LINE: " << line << endl;
    padout(solve(0,0));
    cout << endl;
  }
  return 0;
}

