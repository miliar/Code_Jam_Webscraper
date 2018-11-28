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

int N;
vvi wds;

vi points;

void solve1(vi & x, int *ord){
  if(*ord<0) return;
  int o=*ord;
  ord++;

  vi y[1024];
  rep(i,x.size()){
    int k=x[i];
    y[wds[k][o]].pb(k);
    //if(wds[k][o]!=0) existNonZero = true;
  }
  bool existNonZero = (y[0].size() != x.size());
  if(existNonZero){
    rep(i,y[0].size()){
      int k=y[0][i];
      points[k]++;
    }
  }
  rep(j,1024){
    if(y[j].empty()) continue;
    solve1(y[j],ord);
  }
}

int solve(string order){
  int ord[32];
  ord[0]=26;
  rep(i,26) ord[i+1]=order[i]-'a';
  ord[27]=-1;
  //points.clear();
  points.resize(N);
  rep(i,N) points[i]=0;
  vi x(N);
  rep(i,N) x[i]=i;
  solve1(x,ord);

  int best=-1;
  int bestPos;
  //cout<<endl;
  rep(i,N){
    //cout<<i<<' '<<points[i]<<endl;
    if(points[i]>best){
      best=points[i];
      bestPos=i;
    }
  }
  return bestPos;
}

int main(){
  int T=nextInt();
  repi(cases,1,T){
    N=nextInt();
    int M=nextInt();
    vs words(N);
    rep(i,N) words[i]=next();
    //wds.clear();
    wds.resize(N);
    rep(i,N){
      wds[i].resize(27);
      int len=wds[i][26]=words[i].size();
      rep(j,26){
	wds[i][j]=0;
      }
      rep(k,len){
	wds[i][ words[i][k]-'a' ] |= 1<<k;
      }
    }
    //rep(i,N){rep(j,27) cout<<wds[i][j]<<' '; cout<<endl;}cout<<endl;
    cout<<"Case #"<<cases<<":";
    rep(j,M) {
      cout<<' '<<words[solve(next())];
    }
    //int ans=solve(0,P-1,0);
    //cout<<"Case #"<<cases<<": ";
    //cout<<ans;
    cout<<endl;
  }
  return 0;
}
