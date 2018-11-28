#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n,k;
    cin>>n>>k;
    int ct = 1<<n;
    k = k%ct;
    cout << "Case #" << (i+1) << ": " << (k == (ct-1) ? "ON" : "OFF")<<endl;
  }
}

