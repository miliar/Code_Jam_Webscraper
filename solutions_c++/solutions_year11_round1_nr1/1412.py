#include <iostream>
#include <vector>
#include <string>

using namespace std;

int gcd(int a, int b) {
  if(a>b) return (b, a);
  if(a==b) return a;
  if(a==0) return b;
  return gcd(b%a, a);
}

bool solve()
{
  int N, Pd, Pg;
  cin >> N >> Pd >> Pg;
  if(Pd==0) {
    return (Pg!=100);
  } else if(Pd==100) {
    return (Pg!=0);
  } else {
    int g = gcd(Pd, 100);
    if((Pd%g) != 0) cout << "error";
    //cout << "min " << Pd << " " << g << " " << Pd/g << endl;
    return ((100/g) <= N) && (Pg!=100) && (Pg!=0);
  }
  cout << "error";
}

int main()
{
  int N;
  cin >> N;
  for(int i=0;i<N;i++) {
    cout << "Case #" << (i+1) << ": ";
    bool b = solve();
    if(b) cout << "Possible";
    else cout << "Broken";
    cout << endl;
  }
}