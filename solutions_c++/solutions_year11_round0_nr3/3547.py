#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  int t, n;

  cin >> t;

  for(int i = 0; i < t; i++){
    cin >> n;

    int sum = 0;
    int x = 0;
    int minimum = 100000000;
    for(int j = 0; j < n; j++){
      int a;
      cin >> a;
      minimum = min(minimum, a);
      sum += a;
      x = x ^ a;
    }

    if(x == 0)
      cout << "Case #" << i + 1 << ": " << sum - minimum << endl;
    else
      cout << "Case #" << i + 1 << ": NO" << endl;
  }
  return 0;
}
