#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

/*** recursion GCD ***/
int
gcd(int u, int v)
{
  if(v == 0) return u;
  return gcd(v, u%v);
}

int
exegcd(vector<int>& v, int t0, int t)
{
  if(t+1 >= v.size()) return t0;
  return exegcd(v, gcd(t0, v[t]), t+1);
}

int
main()
{
  int c;
  cin>>c;

  for(int i = 0; i < c; i++){
    int n;
    cin>>n;
    vector<int> v;
    for(int j = 0; j < n; j++){
      int t;
      cin>>t;
      v.push_back(t);
    }
    sort(v.begin(), v.end());

    vector<int> vv;
    for(int j = 1; j < n; j++){
      vv.push_back(v[j] - v[j-1]);
    }

    int a;
    if(n < 3) a = vv[0];
    else a = exegcd(vv, gcd(vv[0], vv[1]), 2);

    int ans = 1000000000;
    for(int j = 0; j < n; j++){
      int b;
      for(b = v[j]*-1; b < 0; b+=a);
      ans = min(ans, b);
    }

    
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }

}
