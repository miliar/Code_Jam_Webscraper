#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int mylog(long long n, int prime) {
  int res = 1;
  for(long long c=prime;;res++){
    if(c > n/prime) break;
    c *= prime;
    if(c > n) break;
  }
  return res;
}

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){

    long long n;

    cin >> n;

    if(n==1){
      cout << "Case #" << tcase << ": " << 0 << '\n';
      continue;
    }
    
    int sq = sqrt(n);
    vector<bool> prime(sq+1);

    prime[0] = prime[1] = false;

    for(int i=2;i<=sq;i++) 
      prime[i] = true;
    
    int sol = 1;
    
    for(int i=0;i<=sq;i++)
      if(prime[i] == true){
	sol += mylog(n, i)-1;
	for(int j=2;j<=sq/i;j++)
	  prime[i*j] = false;
      }
    
    

    cout << "Case #" << tcase << ": " << sol << '\n';
  }
}
