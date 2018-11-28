#include<iostream>
using namespace std;

int a[30];

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int t; cin >> t;
  a[0] = 1;
  for (int i = 1; i <= 30; ++i) a[i] = a[i-1]*2;
  for (int i = 1; i <= t; ++i) {
    int n, k;
    cin >> n >> k;
    cout << "Case #" << i << ": ";
    if (k % a[n] == a[n]-1) cout << "ON"; else cout << "OFF";
    cout << endl;
  }
  return 0;
}
