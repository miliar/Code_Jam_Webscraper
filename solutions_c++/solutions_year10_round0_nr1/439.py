#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()


main(){
  int tc=1,te;
  cin>>te;
  while(te--){
    int n,k;
    cin>>n>>k;
    cout << "Case #" << tc++ << ": " << ((k%(1<<n))==(1<<n)-1?"ON":"OFF") << endl;
  }
}
