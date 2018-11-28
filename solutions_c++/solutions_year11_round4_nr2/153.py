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

int data[512][512];
int sum0[512][512],xsum[512][512],ysum[512][512];

int slidesum(int d[512][512],int x0,int x1,int y0,int y1){
  x1++;y1++;
  return d[x1][y1] - d[x0][y1] - d[x1][y0] + d[x0][y0];
}

int tos(int d[512][512],int x,int y,int k){
  k--;
  int a=slidesum(d,x+1,x+k-1,y,y+k);
  int b=slidesum(d,x,x+k,  y+1,y+k-1);
  int c=slidesum(d,x+1,x+k-1,y+1,y+k-1);
  return a+b-c;
}

int solve(int R, int C){
  repi(x,0,R) repi(y,0,C){
    if(x==0||y==0){
      sum0[x][y]=xsum[x][y]=ysum[x][y]=0;
    }else{
      sum0[x][y] = sum0[x-1][y]+sum0[x][y-1]-sum0[x-1][y-1] + data[x-1][y-1];
      xsum[x][y] = xsum[x-1][y]+xsum[x][y-1]-xsum[x-1][y-1] + (x-1)*data[x-1][y-1];
      ysum[x][y] = ysum[x-1][y]+ysum[x][y-1]-ysum[x-1][y-1] + (y-1)*data[x-1][y-1];
    }
  }
  /*
  rep(x,R){ rep(y,C) { cout<<data[x][y]<<' '; }cout<<endl;}
  rep(x,R+1){ rep(y,C+1) { cout<<sum0[x][y]<<' '; }cout<<endl;}
  rep(x,R+1){ rep(y,C+1) { cout<<xsum[x][y]<<' '; }cout<<endl;}
  rep(x,R+1){ rep(y,C+1) { cout<<ysum[x][y]<<' '; }cout<<endl;}
  */
  int best=-1;
  rep(x,R) rep(y,C){
      int kMax = min(R-x,C-y);
      repi(k,3,kMax){
	int a=tos(sum0,x,y,k);
	int b=tos(xsum,x,y,k);
	int c=tos(ysum,x,y,k);
	/*
	cout<<x<<' ';
	cout<<y<<' ';
	cout<<r<<' ';
	cout<<a<<' ';
	cout<<b<<' ';
	cout<<c<<' ';
	cout<<endl;
	*/
	if(a*(x+x+k-1)==2*b && a*(y+y+k-1)==2*c){
	  best = max(best,k);
	}
      }
  }
  return best;
}

int main(){
  int T=nextInt();
  repi(cases,1,T){
    int R=nextInt();
    int C=nextInt();
    nextInt();
    rep(x,R){
      string s = next();
      rep(y,C){
	data[x][y]=s[y]-'0';
      }
    }
    int ans=solve(R,C);
    cout<<"Case #"<<cases<<": ";
    if(ans<0) cout<<"IMPOSSIBLE";
    else cout<<ans;
    cout<<endl;
  }
  return 0;
}
