#include <iostream>

using namespace std;

int main(){
  int runs;
  cin >> runs;
  for (int C=1; C<=runs; C++){
    cout << "Case #"<<C<<": ";

    int n;
    cin >> n;
    int a[n], b[n];
    for (int i=0; i<n; ++i){
      cin >> a[i];
    }
    for (int i=0; i<n; ++i){
      cin >> b[i];
    }

    sort(a, a+n);
    sort(b, b+n);
    long long answer = 0;
    for (int i=0; i<n; ++i){
      answer += a[i]*b[n-i-1];
    }
    cout << answer << endl;
  }
  return 0;
}
