#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toStr(T x) {stringstream ss; ss << x;string s; return ss.str();}
inline int powi(int n,int p){ int res=1; for(int i=0;i<p;i++) {res = res*n;} return res; } //no overflow check
template<class T> inline T sqr(T x) {return x*x;}

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

int check(vector<int> X){
  int i=0;
  while(1){
    while(i<4 && X[i] != 1) i++;
    //cout << i << endl;
    if (i<4){
      if (X[i] * X[i+4] * X[i+8] * X[i+12] == 1) return 1;
      else i++;
    }else{
      int j = 0;
      while(1){
	while(j<4 && X[j*4] != 1) j++;
	if (j<4){
	  if (X[j*4] * X[j*4+1] * X[j*4+2] * X[j*4+3] == 1) return 1;
	  else j++;
	}else{
	  if (X[0]*X[5]*X[10]*X[15] == 1) return 1;
	  else if (X[3]*X[6]*X[9]*X[12] == 1) return 1;
	  else return 0;
	}
      }
    }
  }
}



int main(void){
  ifstream ifs("input.txt");
  string buf;
  getline(ifs,buf);
  int cases = toInt(buf);
  for(int i=0; i<cases; i++){
    vector<int> X(16,0);
    vector<int> O(16,0);
    int filled = 0;
    for(int j=0; j<4; j++){
      getline(ifs,buf);
      for(int k =0; k< (int)buf.size(); k++){
	if(buf[k] == 'X') {X[4*j+k]=1; filled++;}
	else if(buf[k] == 'O') {O[4*j+k]=1; filled++;}
	else if(buf[k] == 'T') {X[4*j+k]=1; O[4*j+k]=1; filled++;}
      }
    }
    // for(int p=0; p<4; p++){
    //   for(int q=0; q<4; q++){
    // 	cout << X[p*4+q];
    // }
    //   cout << endl;
    // }
    // for(int p=0; p<4; p++){
    //   for(int q=0; q<4; q++){
    // 	cout << O[p*4+q];
    // }
    //   cout << endl;
    // }

      if(check(X)==1) cout << "Case #" << i+1 <<": X won" << endl;
      else if (check(O)==1) cout << "Case #" << i+1 <<": O won" << endl;
      else if (filled < 16) cout << "Case #" << i+1 << ": Game has not completed" << endl;
      else if (filled ==16) cout << "Case #" << i+1 << ": Draw" << endl;
      getline(ifs,buf);
    }
  return 0;
}
