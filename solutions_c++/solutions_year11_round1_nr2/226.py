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

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int N , M;
    cin>>N>>M;
    vector<string> D(N),L(M);
    FOR(i,N) cin>>D[i];
    FOR(i,M) cin>>L[i];
    string ans;
    FOR(t,M){
      string s = L[t];
      int minv = -1 , min_idx = -1;
      string mins;
      FOR(i,N){
        string target = D[i];
        int cost = 0 ; 
        string now = string(SZ(target) , '_');
        string r;
        FOR(j,SZ(s)){
          char c = s[j];
          bool doit = false;
          FOR(k,N){
            if(SZ(D[k]) != SZ(target)) continue;
            if(D[k].find(c) == string::npos) continue;
            /*bool cand = true;
            FOR(p,SZ(now)){
              if(now[p] != '_' && now[p] != D[k][p]){
                cand = false; 
                break;
              }
              if(now[p] == '_'){
                if(r.find(D[k][p]) != string::npos){
                  cand = false;
                  break;
                }
              }
              }
              if(!cand) continue;*/
            string test = string(SZ(target) , '_');
            FOR(p,SZ(r)) {
              FOR(p2,SZ(D[k])){
                if(D[k][p2]==r[p]) test[p2] = r[p] ; 
              }
            }
            if(test == now){
              doit = true;
            }
          }

          if(doit){
            int revealed = 0 ;
            FOR(k,SZ(now)){
              if(target[k] == c) {
                if(now[k]!='_') abort();
                now[k] = c ; 
                revealed++;
              }
            }
            r += c;
            if(revealed==0){
              cost++;
            }
          }
          if(now == target) break;
        }
        if(minv < cost){
          minv = cost;
          min_idx = i ; 
        }
        //        cout<<target<<" "<<cost<<endl;
      }
      if(SZ(ans)) ans += " " ; 
      if(min_idx==-1) abort();
      ans += D[min_idx];
    }
    printf("Case #%d: %s\n" , case_no++ , ans.c_str());
    
  }
  return 0 ;
}
