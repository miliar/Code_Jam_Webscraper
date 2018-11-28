#include<iostream>
using namespace std;

const int maxn = 30+3;

int a[maxn];
int n, k, cases;

int main()
{
    freopen("A1.in","r",stdin);
    freopen("A.out","w",stdout);
    a[0] = 1;
    for (int i = 1; i <= maxn; ++i) a[i] = a[i-1]*2;
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {
      cout << "Case #" << i << ": ";
      cin >> n >> k;
      k %= a[n];
      if (k == a[n]-1) cout << "ON";
      else cout << "OFF";
      cout << endl;
    }
    return 0;
}
