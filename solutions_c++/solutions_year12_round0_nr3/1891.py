#include<iostream>
#include<map>
#include<cmath>
using namespace std;

int rotate(int a, int n) {
  return a / 10 + (a % 10) * pow(10, n);
}
main() {
  int t, a, b;
  map<int, int> l;
  cin>>t;
  for (int i = 0; i < t; i++) {
    cin>>a>>b;
    int n = 0;
    int x = b;
    while (x > 9) {
      x /= 10;
      n++;
    }
    int total = 0;
    l.clear();
    for (int j = a; j <= b; j++) {
      int c = j;
      int q = 1;
      l[c] = 1;
      for (int p = 0; p < n; p++) {
      	int k = rotate(c, n);
        c = k;
        if (l.count(k))
	  continue;
        if (k >= a && k <= b) {
           l[k] = 1;
	   q++;
        }
      }
      total += (q * (q - 1)) / 2;
    }
    cout<<"Case #"<<i + 1<<": "<<total<<endl;
  }
}
