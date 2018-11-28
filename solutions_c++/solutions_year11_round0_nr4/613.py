#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define fr(i,c) for(__typeof (c.begin()) i=c.begin(); i!=c.end(); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long ll;

int main(){
  int t; cin>>t;
  rep(it,t){
    cerr<<"case "<<it+1<<endl;
    int n, a, cnt=0; cin>>n;
    rep(i,n){
      cin>>a;
      if(a==i+1)cnt++;
    }
    printf("Case #%d: %.9f\n", it+1, (double)n-cnt);
  }
  return 0;
}
