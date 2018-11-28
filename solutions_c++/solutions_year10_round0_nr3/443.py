#include<iostream>
#include<set>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define pb push_back
typedef long long ll;
typedef vector<ll> vint;

ll solve(int r,int k,int n,int *in){
  set<int> S;//start person
  int detect[n];
  rep(i,n)detect[i] = -1;
  vint sum;
  int loopbase = 0;

  int p = 0;
  rep(i,r){
    int tmp =p;
    ll people=0;

    if (S.find(p) != S.end()){
      loopbase = detect[p];
      break;
    }
    S.insert(p);

    do{
      if (people+in[tmp] >k)break;
      people+=in[tmp];
      tmp=(tmp+1)%n;
    }while(tmp != p);
    sum.pb(people);
    detect[p] = sum.size()-1;  
    
    p = (tmp)%n;
  }




  ll ret = 0;
  rep(i,loopbase){
    ret+= sum[i];
  }

  r -=loopbase;
  int loopsize = sum.size() - loopbase;
  
  rep(i,loopsize){
    ret+= sum[loopbase+i]*(r/loopsize);
    if (i < r%loopsize)ret+=sum[loopbase+i];
  }


  return ret;
}


main(){
  int tc=1,te;
  cin>>te;
  while(te--){
    int r,k,n;
    cin>>r>>k>>n;
    int in[n];
    rep(i,n){
      cin>>in[i];
    }
    cout << "Case #" << tc++ << ": " << solve(r,k,n,in) << endl;
  }
}
