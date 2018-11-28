#define MOD 1000003
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>

using namespace std;

#define iter(c) __typeof((c).begin())

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define repd(i,n) for(int i=(int)(n); i-->0;)
#define repi(i,a,b) for(int i=(int)(a); i<=(int)(b); i++)
#define times(n) for(int __times=(n); __times-->0;)
#define each(i, c) for (iter(c) i = (c).begin(); i != (c).end(); ++i)

#define all(a) (a).begin(),(a).end()
#define elem(e, c) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define fst first
#define snd second

#define INF 1001001001
#define INFTY (INF<<32LL|INF)
#define EPS 1e-9
#define PI 3.141592653589793

typedef long long ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<string> vs;

template <class T>
void debug(vector<T> v){ each(i,v.size()) cout<<*i<<" "; cout<<endl; }

int nextInt(){ int t; scanf("%d", &t); return t; }
string next(){ string t; cin>>t; return t; }

int R,C;

int loopcnt[10009];
int uft[10009];

void uft_do(int i,int j){
  while(uft[i]>=0) i=uft[i];
  while(uft[j]>=0) j=uft[j];
  if(i==j){
    loopcnt[i]++;
    return;
  }
  if(uft[i]>uft[j]) swap(i,j);
  loopcnt[i]+=loopcnt[j];
  loopcnt[j]=0;
  uft[i]+=uft[j];
  uft[j]=i;
}

void edge(int i,int j, int k, int l){
  i=(i+R)%R;
  k=(k+R)%R;
  j=(j+C)%C;
  l=(l+C)%C;
  uft_do(i*C+j, k*C+l);
}

int solve(vs dat){
  rep(i,R*C) uft[i]=-1;
  rep(i,R*C) loopcnt[i]=0;
  rep(i,R) rep(j,C){
    switch(dat[i][j]){
      case '-': edge(i,j-1,i,j+1); break;
      case '|': edge(i-1,j,i+1,j); break;
      case '/': edge(i-1,j+1,i+1,j-1); break;
      case '\\': edge(i-1,j-1,i+1,j+1); break;
      default: cerr<<"err"<<endl;
    }
  }
  int ans = 1;
  rep(i,R*C){
    if(uft[i]<0) {
      if(loopcnt[i]!=1) return 0;
      ans*=2;
      ans%=MOD;
    }
  }
  return ans;
}

int main(){
  int T=nextInt();
  repi(cases,1,T){
    R=nextInt();
    C=nextInt();
    vs dat;
    rep(i,R) dat.pb(next());
    cout<<"Case #"<<cases<<": ";
    cout<<solve(dat);
    cout<<endl;
  }
  return 0;
}
