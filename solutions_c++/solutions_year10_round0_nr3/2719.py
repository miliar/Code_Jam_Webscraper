#include<iostream>
using namespace std;
#define N 1000
typedef unsigned long long ull;
ull t,n,cnt,nx;
ull r,k,g[N];

ull getC(){
  if(cnt>=r)return 0;
  ull cost=0,nx=1,sum=g[0];
  //cout << sum << ',';
  for(int i=1; i<n && sum+g[i]<=k ; i++){
    sum+=g[i];
    //cout << g[i] << ',' ;
    nx++;
  }
  // cout << endl;
  nx%=n;
  cost=sum;
  cnt++;
  while(nx!=0 && cnt<r){
    sum=0;
    while(sum+g[nx]<=k){
      sum+=g[nx];
      //  cout << g[nx] << ',' ;
      nx=(nx+1)%n;
    }
    cost+=sum;
    cnt++;
    // cout << endl;
  }
  return cost;
}
  

ull Solve(){
  cin >> r >> k >> n;
  for(int i=0 ; i<n ; i++)cin >> g[i];
  ull cost=0;
  cnt=0;
  cost=getC();
  cost=(r/cnt)*cost;
  cnt=(r/cnt)*cnt;
  cost+=getC();
  return cost;
}

int main(){
  cin >> t;
  for(int i=0 ; i<t ; i++)cout << "Case #" << i+1 << ": " << Solve() << endl;
  return 0;
}
