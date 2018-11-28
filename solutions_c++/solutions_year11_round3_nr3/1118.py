#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <deque>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define INF (int)1e10
typedef long long ll;

int INT( string s ) { int x; stringstream ss(s); ss >> x; return x; }
string STR( int x ) { stringstream ss; ss << x; return ss.str(); }

//!!!!!!!!!!!!!!!!!!  To be modified!!  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//#define HANDIN

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#define SMALL 0
#define LARGE 1
const int TYPE = 0;
 //0: competition, 1: practice
const int PRACTICE = 0;
string PROBLEM="c";
const string ATTEMPT="0";
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ifdef HANDIN
#define cin fin
#define cout fout
#endif
ifstream fin;
ofstream fout;

int FILE_OPEN(){
  if(!PROBLEM.empty()&&PROBLEM[0]<='z'&&PROBLEM[0]>='a'){PROBLEM[0] = PROBLEM[0]-'a'+'A';}
  const string SMALL_FILE_NAME = ((!PRACTICE)?"-small-attempt":"-small-practice");
    const string LARGE_FILE_NAME = ((!PRACTICE)?"-large-attempt":"-large-practice");
  string FILE_SMALL_IN = string(PROBLEM+SMALL_FILE_NAME+ATTEMPT+".in");
  string FILE_SMALL_OUT = string(PROBLEM+SMALL_FILE_NAME+ATTEMPT+".out");
  string FILE_LARGE_IN = string(PROBLEM+"-large.in");
  string FILE_LARGE_OUT = string(PROBLEM+"-large.out");
  if(PROBLEM.empty()){printf("Problem is not defined!\n"); system("pause"); return 0;};
  if(TYPE == SMALL){fin.open(FILE_SMALL_IN.c_str()); if(!fin.is_open()){printf("File cannot be found");system("pause");return 0;};fout.open(FILE_SMALL_OUT.c_str());}
  if(TYPE == LARGE){fin.open(FILE_LARGE_IN.c_str()); fout.open(FILE_LARGE_OUT.c_str());}
  return 1;
}
#define STARTCODE if(!FILE_OPEN()){return 0;};
#ifndef HANDIN
#undef STARTCODE
#define STARTCODE ;
#endif

int gcd(int a, int b){
  if(b==0)return a;
  return gcd(b,a%b);
}

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
int kase =1;

ll a[10001];
ll g[10001];
ll lcm[10001];


int main(){
  STARTCODE

  int t;
  cin >> t;
  ll n,l,h;
  while(t--){
    cin >> n >> l >> h;
    
    REP(i,n){
      cin >> a[i];
    }
    sort(a,a+n);
    g[0] = a[0];
    lcm[0] = a[0];
    FOR(i,1,n){
      lcm[i] = (lcm[i-1]/gcd(a[i], lcm[i-1])*a[i]);
    }
    ll ans=-1;
    REP(i,n){
      bool ok = 1;
      REP(j,n){
        if(lcm[i]%a[j]!=0 && a[j]%lcm[i]!=0){
          ok =0 ;
          break;
        }
      }   
      if(ok && lcm[i] >= l && lcm[i] <=h){
        ans = lcm[i];
        break;
      }
    }
    REP(i,n){
      gcd[i]          
    }
    
    cout << "Case #" << kase++ << ": " ;
    if(ans==-1){
      cout << "NO" << endl;            
    }
    else{
      cout << ans << endl;     
    }
    
  }
  


  return 0;
}


