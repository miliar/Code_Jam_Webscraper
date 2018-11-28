#include <iostream>
using namespace std;

int main() {
  int Q;
  cin >> Q;
  for (int q=1;q<=Q;q++) {
    int n;
    cin>> n;
    int sum = 0;
    int least = 1000000000;
    int xrs = 0;
    for (int i=0;i<n;i++) {
      int v = 0;
      cin >> v;
      sum += v;
      if (v<least) least=v;
      xrs ^= v;
    }
    if (xrs == 0)
      cout << "Case #"<<q << ": " << (sum - least) << endl;
    else
      cout << "Case #"<<q << ": NO"<<endl;
  }

}
