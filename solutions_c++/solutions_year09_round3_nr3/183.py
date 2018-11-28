#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;

map<pair<int,int>,long long> memo;

long long solve(const vector<int> &R,int a,int b)
{
 int nexta = a;
 ++ nexta;
 if(nexta == b){ return 0; }
 map<pair<int,int>,long long>::const_iterator it=memo.find(make_pair(a,b));
 if(it!=memo.end())return it->second;
 long long r=1000000000000000LL;
 for(;nexta!=b;++nexta){
  long long v=R[b]-R[a]-2+solve(R,a,nexta)+solve(R,nexta,b);
  r=min(r,v);
 }
 return memo[make_pair(a,b)]=r;
}

int main( void )
{
 int T;
 cin>>T;
 for(int X=1;X<=T;++X){
  int P,Q;
  cin>>P>>Q;
  vector<int> R(Q+2);
  for(int i=0;i<Q;i++)
   cin>>R[i];
  R[Q]=0;
  R[Q+1]=P+1;
  sort(R.begin(),R.end());
  memo.clear();
  long long belong=solve(R,0,R.size()-1);
  printf("Case #%d: %lld\n",X,belong);
 }
}
