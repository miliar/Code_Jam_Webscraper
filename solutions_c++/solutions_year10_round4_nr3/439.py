// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>
#include<bitset>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

const double PI = 4.0*atan(1.0);

int dat[111][111]; // for small;

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int ans = 0 ;
    int r ; 
    cin>>r;
    memset(dat , 0 , sizeof(dat));
    FOR(i,r){
      int x1,y1,x2,y2;
      cin>>x1>>y1>>x2>>y2;
      FOR3(y,y1,y2+1) FOR3(x,x1,x2+1){
        dat[y][x] = 1;
      }
    }
    while(1){
      ans++;
      int cellnum = 0 ; 
      /*FOR(i,7){
        FOR(j,7) cout << " " << dat[i][j] ;
        cout << endl;
      }        cout << endl;*/
      for(int i=100;i>=0;i--){
        for(int j=100;j>=0;j--){
          int neigh = 0 ;
          if(i-1>=0 && dat[i-1][j]) neigh++;
          if(j-1>=0 && dat[i][j-1]) neigh++;
          if(neigh==2) dat[i][j] = 1;
          if(neigh==0) dat[i][j] = 0;
          cellnum += dat[i][j] ; 
        }
      }
      if(cellnum==0) break;
    }
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
