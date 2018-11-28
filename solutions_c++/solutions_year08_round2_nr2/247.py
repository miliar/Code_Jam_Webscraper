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

ifstream fin("B.in");
ofstream fout("B.out");

int A,B,P;
bool b[1001];
int group[1001];
bool share[1001][1001];
map<int,vi> rawr; //map group to members
vi primes;

void sieve(){
   memset(b,1,sizeof(b));
   b[0]=false;
   b[1]=false;
   int m=sqrt(1001);
   for (int i=2; i<=m; i++)
     if (b[i])
       for (int k=i*i; k<=1001; k+=i)
	 b[k]=false;
} 

void subsolve(){
  rawr.clear(); CLR(group); CLR(share); primes.clear();
  int tempP;
  fin>>A>>B>>tempP;
  P=tempP;
  FOR(i,A,B+1){
    group[i]=i;
    rawr[i].pb(i);
  }
  for(int k=P;k<=B;k++)
    if(b[k]) primes.pb(k);
  int l=primes.size();
  FOR(i,A,B)
    FOR(j,i+1,B+1)
    REP(k,l) if(i%primes[k]==0 && j%primes[k]==0) share[i][j]=share[j][i]=1;
  FOR(i,A,B)
    FOR(j,i,B+1){
    if(i==j || group[i]==group[j]) continue;
    if(share[i][j]){
      vi v=rawr[group[j]]; //merge j into i
      REP(l,v.size()){
	group[v[l]]=group[i];
	rawr[group[i]].pb(v[l]);
      }
    }
  }
  //count number of groups
  int ct=0; bool done[B+1]; CLR(done);
  FOR(i,A,B+1){
    if(!done[group[i]]){
      ct++;
      done[group[i]]|=1;
    }
  }
  fout<<ct<<endl;
}

void input(){
  int c; fin>>c;
  sieve();
  REP(i,c){
    fout<<"Case #"<<i+1<<": ";
    subsolve();
  }
}

main(){
  input();
}
