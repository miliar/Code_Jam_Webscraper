#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int t;
  cin >> t;

  for(int i = 1; i <= t; i++){
    int n;
    cin >> n;

    int orange, blue, ot, bt;
    orange = blue = 1;
    ot = bt = 0;
    for(int j = 1; j <= n; j++){
      char c;
      int num;
      cin >> c >> num;

       if(c == 'O'){
        int cost = abs(num-orange)+1;
        if(ot+cost <= bt) ot = bt + 1;
        else ot = ot + cost;
        orange = num;
      }

       if(c == 'B'){
        int cost = abs(num-blue)+1;
        if(bt+cost <= ot) bt = ot + 1;
        else bt = bt + cost;
        blue = num;
      }
    }
    int total = max(ot, bt);
    cout << "Case #" << i << ": " << total << "\n";
  }

  return 0;
}
