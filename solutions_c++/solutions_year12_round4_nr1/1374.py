#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; ++i)
#define MAX 10010

int T, N, d[MAX], l[MAX], D, done[MAX][MAX], ok;

void dfs(int s, int prev, int held){
  if(s == N-1)
    ok = 1;
  if(ok)
    return;
  done[s][prev] = 1;
  FOR(i,s+1,N){
    if(d[i]-d[s] > held)
      break;
    if(!done[i][s])
      dfs(i, s, min(l[i], d[i]-d[s]));
  }
}

int main(){
  
  cin>>T;
  FOR(j,0,T){
    ok = 0;
    cin>>N;
    FOR(i,0,N)
      cin>>d[i]>>l[i];
    cin>>D;
    d[N] = D;
    l[N] = 1;
    N++;
    FOR(i,0,N)
      FOR(k,0,N)
	done[i][k] = 0;
    dfs(0, 0, min(d[0], l[0]));
    if(ok)
      cout<<"Case #"<<j+1<<": "<<"YES"<<endl;
    else
      cout<<"Case #"<<j+1<<": "<<"NO"<<endl;
  }
  
  return 0 ;
  
}