#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
using namespace std;
#define inf 1000000000
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a-1;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define SORT(a) sort(ALL(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef double dbl;

ifstream fin("C.in");
ofstream fout("C.out");

int K;
vi indices;
int val[5000];

void go(){
  int it=0; REP(i,5000) val[i]=-1;
  int nextval=2;
  val[0]=1;
  while(nextval<=K){
    int ct=0;
    while(ct<nextval){
      it++;
      ct++;
      if(it==K) it=0;
      while(val[it]!=-1){
	it++;
	if(it==K) it=0;
      }
    }
    val[it]=nextval;
    nextval++;
  }
  int k=indices.size();
  REP(i,k-1)
    fout<<val[indices[i]-1]<<' ';
  fout<<val[indices[k-1]-1]<<endl;
}

void solve(){
  CLR(val); indices.clear();
  int n;
  fin>>K>>n;
  REP(i,n){
    int x;
    fin>>x; indices.pb(x);
  }
  go();
}

void input(){
  int T; fin>>T;
  REP(i,T){
    fout<<"Case #"<<i+1<<": ";
    solve();
  }
}

main(){
  input();
  solve();
  return 0;
}
