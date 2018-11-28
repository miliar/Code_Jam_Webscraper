#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
  ifstream cin("C-small-attempt0 (1).in");
  ofstream cout("out.txt");
  int C;
  cin >> C;
  for(int c = 0; c < C; c++) {
    vector<vector<int> > binom;
    binom.push_back(vector<int>());
    binom[0].push_back(1);
    binom.push_back(vector<int>());
    binom[1].push_back(1);
    binom[1].push_back(1);
    for(int n = 2; n <= 500; n++) {
      vector<int> tmp(n+1);
      tmp[0] = tmp[n] = 1;
      for(int k = 1; k < n; k++)
        tmp[k] = (binom[n-1][k-1] + binom[n-1][k]) % 100003;
      binom.push_back(tmp);
    }
    int n = 0;
    cin >> n;
    int res = 0;
    vector<vector<int> > table;
    for(int i = 2; i <= n; i++) {
      vector<int> tmp(i);
      tmp[1] = 1;
      for(int j = 2; j < i; j++) {
        for(int k = 1; k <= i-j; k++) {
          if(j-k < 1)
            break;
          tmp[j] += (binom[i-j-1][k-1] * table[j-2][j-k]) % 100003;
        }
        tmp[j] %= 100003;
      }
      table.push_back(tmp);
    }
    cout << "Case #" << c+1 << ": ";
    for(int i = 0; i < n; i++)
      res += table[n-2][i];
    res %= 100003;
    cout << res;
    cout << endl;
  }
}
