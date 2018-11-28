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
    int n, a[1000], s=0, sum=0; cin>>n;
    rep(i,n)cin>>a[i], s^=a[i], sum+=a[i];
    sort(a,a+n);
    sum-=a[0];

    cout<<"Case #"<<it+1<<": ";
    if(s!=0)cout<<"NO"<<endl;
    else cout<<sum<<endl;
  }
  return 0;
}
