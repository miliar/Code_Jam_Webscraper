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
#define SZ(a) a.size()
#define LEN(a) a.length()
#define pb push_back
typedef long long ll;
typedef double dbl;

struct trip{
  int depart,arrive;
};

ifstream fin("B-large.in");
ofstream fout("B-sol.txt");

int T,A,B;
vector<trip> vA,vB; //vA - A to B, vB - B to A
bool done[100][2];

bool cmp(const trip t1,const trip t2){
  if(t1.depart==t2.depart) return t1.arrive<t2.arrive;
  return t1.depart<t2.depart;
}

//t is time train is at station
//train has NOT been sent yet
void send(int t,bool b){ //true if at A
  if(b){ //FIND LOWEST A DEPART
    REP(i,A) if(vA[i].depart>=t && !done[i][b]){
      send(vA[i].arrive+T,!b);
      done[i][b]|=1;
      return;
    }
  }
  else{
    REP(i,B) if(vB[i].depart>=t && !done[i][b]){
      send(vB[i].arrive+T,!b);
      done[i][b]|=1;
      return;
    }
  }
}

void solve(){
  int n[2]; n[0]=n[1]=0;
  memset(done,0,sizeof(done));
  while(true){
    //find lowest available departure time not yet done
    trip t; t.depart=1440; t.arrive=1440;
    bool b;
    REP(i,A) if(!done[i][1] && cmp(vA[i],t)){
      t=vA[i]; b=1; break;
    }
    REP(i,B) if(!done[i][0] && cmp(vB[i],t)){
      t=vB[i]; b=0; break;
    }
    if(t.depart==1440) break;
    //if send a first, b is true
    send(0,b); n[b]++;
  }
  fout<<n[1]<<' '<<n[0]<<endl;
}

int convert(string s){
  int h=atoi(s.substr(0,2).c_str());
  int m=atoi(s.substr(3).c_str());
  return 60*h+m;
}

main(){
  int N; fin>>N;
  REP(i,N){
    fin>>T;
    fin>>A>>B;
    string a,b;
    REP(j,A){
      fin>>a>>b;
      trip t; t.depart=convert(a); t.arrive=convert(b);
      vA.pb(t);
    }
    REP(j,B){
      fin>>a>>b;
      trip t; t.depart=convert(a); t.arrive=convert(b);
      vB.pb(t);
    }
    sort(ALL(vA),cmp); sort(ALL(vB),cmp);
    fout<<"Case #"<<i+1<<": ";
    solve();
    vA.clear(); vB.clear();
  }
}
