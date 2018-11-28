#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int a[1005],b[1005];

int gcd(int x,int y){
  if (y==0)
    return x;
  return gcd(y,x%y);
}
int main(){
  int t,o;
  cin >> t;
  o = t;
  while (t--){
    cout << "Case #" << o-t <<": ";
    int n;
    cin >> n;
    for (int i = 0; i < n;  ++i)
      cin >> a[i];
    sort(a,a+n);
    for (int i = 1; i < n; ++i)
      b[i-1] = a[i]-a[i-1];
    if (n==2){
      int ans = a[0]%b[0];
      if (ans!=0)
	ans = b[0]-ans;
      cout <<ans<<endl;
    }else{
      // find gcd of b
      int g =gcd(b[0],b[1]);
      for (int i = 2; i < n-1; ++i)
	g = gcd(g,b[i]);
      // all a mod b, and then b-a
      int ans = a[0]%g;
      if (ans==0)
	cout << ans <<endl;
      else{
	ans = g-ans;
	cout << ans <<endl;
      }
    }
  }
}
