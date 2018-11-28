#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <climits>
#include <sstream>
#include <cmath>
using namespace std;

#define MAXN 1008

typedef long long ll;
ll t[MAXN];

int tcase;
int n;

ll gcd(ll a, ll b){
 if(!b) return a;
 return gcd(b,a%b);
}

int main(){
  
  freopen("B-small-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);  
    
  cin>>tcase;
  for(int i=1;i<=tcase;++i){
    cin>>n;
    for(int j=0;j<n;++j) cin>>t[j];
    ll gd = abs(t[1]-t[0]); ll r;
    for(int j=1;j<n-1;++j) gd = gcd(gd,abs(t[j+1]-t[j]));

    if(t[0]%gd==0){
      r = 0;
    }
    else {
      r = gd-t[0]%gd;
    }
    printf("Case #%d: ",i);
    cout<<r<<endl;
    
     
   
  } 
  return 0;
}
