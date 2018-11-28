#include <iostream>
#include <vector>
#include <utility>
#include <string>

using namespace std;

typedef long long ll;

ll gcd (ll a, ll b){
  if(a < b) swap(a, b);
  if(a % b == 0) return b;
  return gcd(a %b, b);
}


string  solve(ll n, int pd, int pg){
  if(pg == 0){
    if(pd == 0) return "YES";
    else return "NO";		  
  }
  if(pg == 100){
    if(pd == 100) return "YES";
    else return "NO";		  
  }
 


  ll g = gcd(100, pd);
  ll N = 100 / g;
  if( N <= n) return "YES";
  else return "NO";

}


int main(){
  int t;cin >> t;
  for(int i = 1;i<=t;i++){
    ll n;
    int pd, pg;
    cin >> n >> pd >> pg ;

    string ans = solve(n, pd, pg);
    if(ans == "YES") ans = "Possible";
    else ans = "Broken";
		       
    cout << "Case #" << i << ": " << ans <<endl;
  }
  return 0;

}
