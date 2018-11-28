#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>
#define int long long

using namespace std;

bool is_prime(int s){
  if (s == 0 || s == 1)
    return(false);
  for (int i=2;i*i<=s;i++)
    if (s % i == 0)
      return(false);
  return(true);
}



#undef int
int main(){
#define int long long
  int ttime;
  cin>>ttime;
  vector<bool> pr(1000001);
  for (int i=1;i<pr.size();i++)
    pr[i]=is_prime(i);
  for (int ccount=1;ccount<=ttime;ccount++){
    int n;
    cin>>n;
    int ans=0;
    for (int i=2;i*i<=n;i++) if (pr[i]){
      int temp=i;
      while (temp <= n/i){
	temp*=i;
	ans++;
      }
    }
    if (n >= 2)
      ans++;
    cout<<"Case #"<<ccount<<": "<<ans<<endl;
  }
}
