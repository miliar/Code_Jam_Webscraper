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

ll_t X,S,R,T,N;

double take(double D , double &run_time , double W)
{
  if(D==0) return 0;
  if(run_time == 0){
    return D / (S + W);
  }else{
    /*
      NORMAL * (S + W) + RUN_TIME * (R + W) = X
     */
    double lower = 0 , upper = run_time;
    double ret = -1;
    FOR(_,100){
      double RUN_TIME = (lower + upper) / 2.0;
      double NORMAL = (D - RUN_TIME * (R + W)) / (S + W);
      if(NORMAL >= 0){
        if(lower == RUN_TIME) break;
        lower = RUN_TIME;
        ret = NORMAL + RUN_TIME ; 
      }else{
        if(upper == RUN_TIME) break;
        upper = RUN_TIME;
      }
    }
    //cout<<" "<<D<<" "<<run_time<<" "<<lower<<" "<<ret<<" "<<W<<endl;
    run_time -= lower;

    return ret;
  }
  return 0 ;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    cin>>X>>S>>R>>T>>N;
    double time = 0 ;
    vector<int> B(N),E(N),W(N);
    int WL = X;
    double run_time = T;
    vector<pair<int,int> > dat;
    FOR(i,N){
      scanf("%d%d%d",&B[i],&E[i],&W[i]);
      int D = E[i] - B[i] ; 
      WL -= D;
      dat.push_back(MP(W[i] , D));
    }
    sort(ALL(dat));
    time += take(WL,run_time,0);

    FOR(i,SZ(dat)){
      time += take(dat[i].second,run_time,dat[i].first);
    }

    printf("Case #%d: %.10f\n" , case_no++ , time);
  }
  return 0 ;
}
