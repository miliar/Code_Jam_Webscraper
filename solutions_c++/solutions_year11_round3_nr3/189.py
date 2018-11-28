#include <iostream>
using namespace std;
int gcd(int x ,int y){
  if (y==0) return x;
  return gcd(y,x%y);
}
int lcm(int x,int y){
  return x/gcd(x,y)*y;
}
long long a[10005];
int main(){
  int t;
  cin >> t;
  for (int kk=1;kk<=t;++kk){
    cout << "Case #"<<kk<<": ";
    long long n,l,h;
    cin >>n>>l>>h;
    for (int i = 0; i < n; ++ i)
      cin >> a[i];
    long long lcmm = a[0];
    for (int i = 1;i <n;++i)
      lcmm = lcm(lcmm,a[i]);

    bool ok = false;
    for (int i = l; i <=h; ++i){
      ok = true;
      for (int j = 0; j <n;++j){
	if (!(i%a[j]==0||a[j]%i==0)){
	  ok = false;
	  break;
	}
      }
      if (ok){
	cout << i << endl;
	break;
      }
    }

    if (!ok)
      cout << "NO\n";
  }
}
