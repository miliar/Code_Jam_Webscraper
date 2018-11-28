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

bool solve(ll_t N , ll_t PD , ll_t PG)
{
  if(PG == 100){
    return PD == 100;
  }
  if(PG == 0){
    return PD == 0;
  }
  if(N <= 100000){
    // daywin / Day = PD / 100
    // daywin * 100 = PD * day;
    for(ll_t day=1;day<=N;day++){
      ll_t daywin = PD * day ; 
      if(daywin % 100) continue;
      daywin /= 100;
      if(day >= daywin){
        return true;
      }
    }
    return false;
  }
  return true;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    ll_t N, PD , PG;
    cin>>N>>PD>>PG;

    /*
      daywin/Day = PD/100
      (daywin+everwin)/(Day+Ever) = PG/100
      Day <= N
      Day = daywin/(PD/100)

      daywin = PD*Day/100

      (daywin+everwin)*100 = PG * (Day+Ever)
      daywin*100+everwin*100 = PG*Day +PG*Ever
      everwin*100 - PG*Ever = PG*Day-daywin*100
     */
    bool ok = solve(N , PD , PG);

    printf("Case #%d: %s\n" , case_no++ , ok?"Possible":"Broken");
    
  }
  return 0 ;
}
