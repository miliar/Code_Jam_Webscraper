#include <vector>
#include <queue>
#include <map>
#include <set>
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
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef double dbl;

ifstream fin("A.in");
ofstream fout("A.out");

bool andgate[100],change[100];
bool leafval[100];
int start;

bool good(int index,bool val){
  if(index-1>=start) return leafval[index-1]==val;

  if(andgate[index-1]){
    if(val==1)
      return good(index*2,val)&&good(index*2+1,val);
    return good(index*2,val) || good(index*2+1,val);
  }
  if(val==0)
    return good(index*2,val) && good(index*2+1,val);
  return good(index*2,val) || good(index*2+1,val);
}

main(){
  int T; fin>>T; REP(k,T){
    fout<<"Case #"<<k+1<<": ";
    int N; bool V;
    fin>>N>>V; //number of nodes, value we want

    REP(i,(N-1)/2){
      fin>>andgate[i]>>change[i];
    }

    FOR(i,(N-1)/2,N)
      fin>>leafval[i];

    start=(N-1)/2;

    //try each state

    int res=inf;

    REP(mask,1<<start){
      bool yes=true;
      int x=__builtin_popcount(mask);

      if(x>res) continue;

      REP(i,start){
	if(mask&(1<<i)) if(!change[i]) {yes&=0; break;}
      }

      if(!yes) continue;

      REP(i,start)
	if(mask&(1<<i)) andgate[i]^=1;

      if(good(1,V)){
	res=x;
      }

      REP(i,start)
	if(mask&(1<<i)) andgate[i]^=1;
    }


    if(res==inf) fout<<"IMPOSSIBLE"<<endl;
    else fout<<res<<endl;

  }
}

