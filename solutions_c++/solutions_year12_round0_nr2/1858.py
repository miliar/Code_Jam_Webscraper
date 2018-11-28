#include<iostream>
using namespace std;

main() {
  int n;
  cin>>n;
  int t, s, p, a;
  for (int i = 0; i < n; i++) {
    cin>>t>>s>>p;
    int count = 0;
    for (int j = 0; j < t; j++) {
      cin>>a;
      if (a >= 3 * p - 2) {
	count++;
      } else if (3 * p - 4 >= 0 && a >= 3 * p - 4 && s > 0) {
	count++;
	s--;
      }
    }
    cout<<"Case #"<<i + 1<<": "<<count<<endl;
  }
}
	
