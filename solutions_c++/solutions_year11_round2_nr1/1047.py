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

#define HANDIN

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#define SMALL 0
#define LARGE 1
const int TYPE = 1;
 //0: competition, 1: practice
const int PRACTICE = 0;
string PROBLEM="a";
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

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
int kase =1;
char  a[101][101];
int played[101];
int win[101];
double WP[101];
double OWP[101],OOWP[101];

int main(){
  STARTCODE

  int t,n;
  cin >> t;
  
  while(t--){
    cin >> n;
    memset(a,0,sizeof a);
    REP(i,n){
      REP(j,n){
        cin >> a[i][j];        
      }         
    }
    memset(played,0,sizeof played);
    memset(win,0,sizeof win);
    memset(WP,0,sizeof WP);
    memset(OWP,0,sizeof OWP);
    memset(OOWP,0,sizeof OOWP);
    REP(i,n){
      REP(j,n){
        if(a[i][j]=='.')continue;
        else if(a[i][j]=='1')win[i]++;
        played[i]++;
      }
     // cout << "wn = " << win[i] << " " << played[i] << endl;
      WP[i] = (double)win[i]/(double)played[i];
    //  cout << "WP = " << WP[i] << endl;
    }           
    REP(i,n){
      double sum = 0;
      int tmp = 0;
      for(int j =0 ; j < n; j++){
        if(j==i || a[i][j]=='.')continue;
        sum += (win[j] - (a[j][i]=='1'?1:0))/((double)played[j]-1);
        tmp++;
      }
      sum/=(double)(tmp);
      
      OWP[i] = sum;
    }
    REP(i,n){
      double sum = 0;
      int tmp =0 ;
      for(int j =0 ; j < n; j++){
        if(j==i|| a[i][j]=='.')continue;
        sum += OWP[j];
        tmp++;
      }
    //  cout << "tmp = " << tmp << endl;
      sum/=(double)(tmp);
      OOWP[i] = sum;
    }
    cout << "Case #" << kase++ << ":" << endl;
    REP(i,n){
      cout << 0.25*WP[i] + 0.5 *OWP[i]+0.25*OOWP[i] << endl;
    }
  }


  return 0;
}


