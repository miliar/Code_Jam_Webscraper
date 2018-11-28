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

int mod = 10009;

int hist[26]={0};

int eval_sub(string& f)
{
  ll_t ret = 1;
  FOR(i,SZ(f)){
    ret *= hist[(int)(f[i]-'a')];
    ret %= mod;
  }
  return ret % mod;
}

int eval(vector<string>& f)
{
  int ret = 0 ;
  FOR(i,SZ(f)){
    ret += eval_sub(f[i]);
  }
  return ret;
} 

int memo[300][300];

int choose(int s , int t)
{
  if(t==0 || s==t) return 1;
  if(memo[s][t]!=-1) return memo[s][t];
  return memo[s][t] = (choose(s-1,t) + choose(s-1,t-1)) % mod;
}

int mypow(int x, int y)
{
  ll_t ret = 1;
  FOR(i,y) { ret *= x; ret %= mod; }
  return ret;
}

int dfs(vector<string>& f , vector<string>& dic , int K)
{
  if(K==0) {
    //cout << step << endl;
    return eval(f);
  }
  int val = 0 ;
  FOR(i,SZ(dic)){
    FOR(j,SZ(dic[i])) hist[dic[i][j]-'a']++;
    val += dfs(f , dic , K-1);
    val %= mod;
    FOR(j,SZ(dic[i])) hist[dic[i][j]-'a']--;
  }
  return val;
}

int main() {
  int t,case_no=1;
  cin>>t;
  CLS(memo , -1);
  while(t--){
    string s; int K;
    cin>>s>>K;
    vector<string> f;
    replace(ALL(s) , '+' , ' ');
    istringstream in(s);
    string tok; while(in>>tok) f.push_back(tok);
    //FOR(i,SZ(f)) cout << "  " << f[i] << endl;
    int m; 
    cin>>m;
    vector<string> dic(m);
    FOR(i,m) {
      cin>>dic[i];
    }
    
    vector<int> ans(K);

    FOR(i,K){      
      ans[i] = dfs(f,dic,i+1);
    }

    printf("Case #%d:" , case_no++);
    FOR(i,K){
      printf(" %d" , ans[i]);
    }
    puts("");
  }
  return 0 ;
}
