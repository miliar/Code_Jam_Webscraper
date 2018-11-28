// compile with "g++ XXX.cc -O2" in Cygwin (gcc version 4.5.3 (GCC))

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
#include<cassert>

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

int N;
ll_t W,L;
int R[10000];

double aX[10000];
double aY[10000];

int max_turn = 100000;
int turn = 0;

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    cin>>N>>W>>L;
    vector<pair<int, int> > dat;
    FOR(i,N) {
      cin>>R[i];
      dat.push_back(MP(R[i] , i));
    }
    sort(ALL(dat));
    reverse(ALL(dat));
  BEGIN : 
    FOR(ii,N){
      int i = dat[ii].second;
      while(1){
        double x = rand() * 1.0 / RAND_MAX * W;
        double y = rand() * 1.0 / RAND_MAX * L;
        /*if(rand()%10 == 0) x = 0;
        else if(rand()%10 == 1) y = 0;
        else if(rand()%10 == 2) x = W;
        else if(rand()%10 == 3) y = L;*/
        double r = R[i];
        bool ok = true;
        turn++;
        FOR(jj,ii){
          int j =dat[jj].second;
          double x1 = aX[j];
          double y1 = aY[j];
          double r1 = R[j];
          double dis = hypot(x1-x , y1-y);
          if(r + r1 + 1e-3 >= dis){
            ok = false;
            break;
          }
        }
        if(ok){
          aX[i] = x;
          aY[i] = y;
          break;
        }
        if(turn >= max_turn){
          cerr<<"RESET"<<endl;
          turn = 0 ;
          goto BEGIN;
        }
      }
    }

    printf("Case #%d:" , case_no++);
    FOR(i,N) printf(" %.6f %.6f" , aX[i] , aY[i]); puts("");
    
    
  }
  return 0 ;
}
