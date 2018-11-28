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
const string ATTEMPT="1";
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

char a[51][51];
int n,m;

int dx[] = {0,1,1}, dy[] = {1,0,1};

bool in(int x, int y){
  if(x >=0 &&  x < n && y >= 0 && y < m){
    return 1;
  }
  return 0;
}

bool check(int x, int y){
  REP(i,3){
    int nx = x+dx[i];
    int ny = y+dy[i];

    if(!in(nx,ny)){
    //  cout << "HERE" << endl;
      return 0;}
    if(a[nx][ny]!='#'){
     // cout << "HER" << endl;
      return 0;
    }         
  }
  return 1;
}

bool solve(int x, int y){
//  cout << "x = " << x << " y = " << y << " " << a[x][y] << endl;
  if(x == n){
    return 1;
  }
  if(y == m){
    return solve(x+1,0);
  }
 // cout << "a = " << a[x][y] << endl;
  if(a[x][y]!='#'){
    return solve(x,y+1);
  }

  if(check(x,y)){
    a[x][y] = '/';
    a[x][y+1] = '\\';
    a[x+1][y] = '\\';
    a[x+1][y+1] = '/';
    return solve(x, y+1);
  }
  return 0;
}


int main(){
  STARTCODE

  int t;
  cin >> t;
  while(t--){
    cin >> n >> m;
    REP(i,n){
      REP(j,m){
        cin >> a[i][j];         
      }         
    }        
    cout << "Case #" << kase++ << ":" << endl;
    if(solve(0,0)){
      REP(i,n){
        REP(j,m){
          cout << a[i][j];         
        }         
        cout << endl;
      }
    } 
    else{
      cout << "Impossible" << endl;     
    }
  }
  


  return 0;
}


