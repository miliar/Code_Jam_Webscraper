#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
using namespace std;

vector<int> P;
vector<int> R;
int diff(int cp,int dp){
  if(cp<dp) return 1;
  else if(cp > dp) return -1;
  else return 0;
}
int destination(int r,int i){
  for(int j=i;j<(int)P.size();j++){
    if(r==R[j]) return P[j];
  }
  return -1;
}
int main()
{
  int T,CASE = 1;
  scanf("%d",&T);
  while(T--){
    int N;
    scanf("%d",&N);
    int ans = 0;
    int rp[2] ={1,1};
    P.clear();
    R.clear();
    REP(i,N){
      char r;
      int p;
      scanf(" %c %d",&r,&p);
      int tr = 0;
      if(r=='B') tr = 1;
      P.push_back(p);
      R.push_back(tr);
    }
    int n = P.size();
    REP(i,n){
      int d[2];
      d[0] = destination(0,i);
      d[1] = destination(1,i);
      while(1){
	if(P[ i ] == rp[ R[i] ]){
	  rp[(R[i]+1)%2] += diff(rp[(R[i]+1)%2],d[(R[i]+1)%2]); 
	  ans++;
	  break;
	}
	REP(j,2) rp[j] += diff(rp[j],d[j]);
	ans++;
      }
    }
    printf("Case #%d: %d\n",CASE++,ans);
  }
  return 0;
}
