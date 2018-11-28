#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int main(){
  int n;
  string s;
  string c("welcome to code jam");
  cin >> n;
  getline(cin, s);
  for(int i = 0; i < n; ++i){
    getline(cin, s);
    vector< vector<int> > w(c.length(), vector<int>(1 + s.length(), 0));
    for(int j = 1; j < (int) w[0].size(); ++j){
      w[0][j] = w[0][j-1] + (s[j-1] == c[0]);
      w[0][j] %= 10000;
    }
    for(int h = 1; h < (int) w.size(); ++h){
      for(int j = 1; j < (int) w[h].size(); ++j){
        w[h][j] = w[h][j - 1];
        if(s[j-1] == c[h]) w[h][j] += w[h-1][j-1];
        w[h][j] %= 10000;
      }
    }
    cout << "Case #" << 1 + i << ": " << setw(4) << setfill('0') << w[c.length()-1][s.length()] << endl;
  }
}
