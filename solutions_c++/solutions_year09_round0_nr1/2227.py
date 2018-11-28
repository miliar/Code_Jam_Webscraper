#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define repd(i,n) for(int i=(int)(n); i-->0;)
#define repi(i,a,b) for(int i=(int)(a); i<=(int)(b); i++)
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define fst first
#define snd second

#define INFTY 1000000000
#define EPS 1e-9
#define PI 3.141592653589793

typedef long long ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<string> vs;

void debug(vi v){ rep(i,v.size()) cout<<v[i]<<" "; cout<<endl; }

int nextInt(){ int t; cin>>t; return t; }

int main(){
  int L,D,N;
  cin>>L>>D>>N;
  vs words(D);
  rep(i,D) cin>>words[i];
  repi(ncase, 1, N){
    cout<<"Case #"<<ncase<<": ";
    vvi ok(L,vi(26));
    {
      string str;
      cin>>str;
      int i,p;
      p=0;
      rep(i,L){
	if(str[p]!='('){
	  ok[i][str[p]-'a']=1;
	  p++;
	}else{
	  p++; // (
	  while(str[p]!=')'){
	    ok[i][str[p]-'a']=1;
	    p++;
	  }
	  p++; // )
	}
      }
    }
    // cout<<endl; rep(x,ok.size()) debug(ok[x]); cout<<endl;
    int cnt=0;
    rep(k,D){
      bool good=true;
      rep(i,L){
	if(!ok[i][words[k][i]-'a']){
	  good=false;
	}
      }
      if(good) cnt++;
    }
    cout<<cnt<<endl;
  }
  return 0;
}
