#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <set>

using namespace std;

int main() {
  ifstream cin("C-large.in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> p;
    int x = 0;
    for(int i = 0; i < N; i++) {
      int tmp;
      cin >> tmp;
      p.push_back(tmp);
      x ^= tmp;
    }
    sort(p.begin(), p.end());
    cout << "Case #" << t << ": ";
    if(x != 0) {
      cout << "NO";
    } else {
      int sum = 0;
      for(int i = 1; i < p.size(); i++)
        sum += p[i];
      cout << sum;
    }
    cout << endl;
  }
}
