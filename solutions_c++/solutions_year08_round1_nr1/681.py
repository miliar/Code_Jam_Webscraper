#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  vector<long long> x, y;
  int T, n, i, test = 1;
  long long dot, x1, y1;

  cin >> T;

  while(T--){

    cin >> n;

    dot = 0;

    for(i = 0 ; i < n ; i++){
      cin >> x1;
      x.push_back(x1);
    }

    for(i = 0 ; i < n ; i++){
      cin >> y1;
      y.push_back(y1);
    }

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    for(i = 0 ; i < n ; i++)
      dot += (x[i] * y[n - i - 1]);

    cout << "Case #" << test++ << ": " << dot << endl;

    x.clear();
    y.clear();
  }
}
