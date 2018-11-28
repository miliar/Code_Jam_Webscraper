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

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

const double PI = 4.0*atan(1.0);

set<int> memo;

vector<int> is_happy_sum[11];

bool ishappy_precalc(int n , int base)
{
  if(n==1) return true;
  if(n<=0) return false;
  if(memo.count(n)) return false;
  memo.insert(n);
  int sum = 0 ;
  while(n){
    int d = n%base;
    sum += d*d;
    n /= base;
  }
  return ishappy_precalc(sum,base);
}

bool ishappy(int n , int base)
{
  if(n==1) return true;
  if(n<=0) return false;
  //cout << n << " " << base << endl;
  int sum = 0 ;
  while(n){
    int d = n%base;
    sum += d*d;
    n /= base;
  }
  assert(sum <= 1000) ; 
  return sum==1 || binary_search(ALL(is_happy_sum[base]) , sum);
}
int main() {
  FOR(i,11) is_happy_sum[i].clear();
  for(int b=2;b<=10;b++){
    for(int j=2;j<=1000;j++){
      memo.clear();
      if(ishappy_precalc(j , b)){
        is_happy_sum[b].push_back(j);
      }
    }
  }
  int t,case_no=1;
  cin>>t;
  string line;
  getline(cin,line);
  while(t--){
    int ans = -1 ;
    getline(cin,line);
    istringstream in(line);
    VI dat;
    int p;
    while(in>>p) if(p!=2 && p!=4) dat.push_back(p);   
    if(SZ(dat)==7){
      ans = 11814485;
    }else{
      for(int i=2;;i++){
        bool ok = true;
        FOR(j,SZ(dat)){
          //memo.clear();
          if(!ishappy(i , dat[j])){
            ok = false;
            break;
          }
        }
        if(ok){
          ans = i ;
          break;
        }
      }
    }
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
