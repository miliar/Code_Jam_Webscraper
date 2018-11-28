#include<iostream>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)

bool cnt(int ai,int bi,int aj,int bj){
  return (ai < aj && bj < bi) || (ai > aj && bi < bj);
}

int solve(int n,int *a,int *b){
  int ret =0;
  rep(i,n){
    REP(j,i+1,n){
      if (cnt(a[i],b[i],a[j],b[j]))ret++;
    }
  }
  return ret;
}

main(){
  int tc=1,te;
  cin>>te;
  while(te--){
    int n;
    cin>>n;
    int a[n],b[n];
    rep(i,n)cin>>a[i]>>b[i];
    cout << "Case #" << tc++ << ": " << solve(n,a,b) << endl;
  }
}

