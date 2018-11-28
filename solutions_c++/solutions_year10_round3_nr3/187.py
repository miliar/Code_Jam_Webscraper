#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL; 
typedef vector<int> VI; 
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<pair<LL,LL> > VPLL;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS; 
typedef long double LD; 

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;} 
inline LL MIN(LL a, LL b){ return a < b ? a : b;} 

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int N,M,TT;
int B[2150][2150];
int DP[2150][2150];
int A[2150];

string decode(char c){
  if(c =='0')return "0000";
  if(c =='1')return "0001";
  if(c =='2')return "0010";
  if(c =='3')return "0011";
  if(c =='4')return "0100";
  if(c =='5')return "0101";
  if(c =='6')return "0110";
  if(c =='7')return "0111";
  if(c =='8')return "1000";
  if(c =='9')return "1001";
  if(c =='A')return "1010";
  if(c =='B')return "1011";
  if(c =='C')return "1100";
  if(c =='D')return "1101";
  if(c =='E')return "1110";
  if(c =='F')return "1111";
  return "";
}

int rundp(){
  int max = 1, maxj=0,maxi=0;
/*  cout << "BB" << endl;
  FOR(i,N+1){
    FOR(j,M+1){
      cout << B[i][j] << " ";
    }
    cout << endl;
    
  }*/

  FOR(ii,N)FOR(jj,M){
    int i = ii+1;
    int j = jj+1;
    if (B[i][j] == 2){
      DP[i][j] = 0;
      continue;
    }
    if (B[i-1][j] == 2 || B[i][j-1] == 2){
      DP[i][j] = 1;
      continue;
    }
    if (B[i-1][j] != B[i][j] && B[i][j-1] != B[i][j] && B[i][j] == B[i-1][j-1]){ 
      DP[i][j] = MIN(MIN(DP[i-1][j],DP[i-1][j-1]),DP[i][j-1])+1;
      if (DP[i][j] > max){
        max = DP[i][j];
        maxi = i;
        maxj = j;
      }
    }
    else{ DP[i][j] = 1; }
  }
/*
  cout << "DP " << endl;
  FOR(i,N+1){
    FOR(j,M+1){
      cout << DP[i][j] << " ";
    }
    cout << endl;
  }*/

  if (max == 1) return 1;
  FOR(i,max)FOR(j,max){
    B[maxi-i][maxj-j] = 2;
  }
  return max;
}

int main(){
  cin >> TT;
  FOR(tt,TT){
    FOR(i,2145) A[i] = 0;
    cin >> N >> M;
    FOR(i,M+10) B[0][i] = 2;
    FOR(i,N+10) B[i][0] = 2;
    FOR(i,N){
      string s;
      cin >> s;
      FOR(j,s.length()){
        string ss = decode(s[j]);
        //reverse(ss.begin(),ss.end());
        FOR(k,4) B[i+1][j*4+k+1] = ss[k]-'0';
      }
    }
    while(true){
      int ll = rundp();
      if (ll == 1) break;
      A[ll]++;
    }
    int spolu = N*M;

    int typov = 0;
    int w = 2145;
    while(w > 1){
      if (A[w] > 0){
        spolu -= w*A[w]*w;
        typov++;
      }
      w--;
    }
    if (spolu > 0)typov++;
    cout << "Case #" << (tt+1) << ": " << typov << endl;
    w = 2145;
    spolu = N*M;
    while(w > 1){
      if (A[w] > 0){
        cout << w << " " << A[w] << endl;
        spolu -= w*A[w]*w;
      }
      w--;
    }

    if (spolu > 0) cout << 1 << " " << spolu << endl;
  }
  return 0;
}


