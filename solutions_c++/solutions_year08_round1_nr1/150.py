#include<iostream>
#include<algorithm>

using namespace std;

int n;
int a[10000];
int b[10000];

int solve()
{
  int i,n,r;
  cin >> n;
  for (i=0; i<n; i++) {
    cin >> a[i];
    a[i]=-a[i];
  }
  for (i=0; i<n; i++) cin >> b[i];
  sort(a, a+n);
  sort(b, b+n);
  r=0;
  for (i=0; i<n; i++) r-=a[i]*b[i];
  cout << r << endl;
  return 0;
}

int main()
{
  int t, c=0;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ": ";
    solve();
  }
  return 0;
}
