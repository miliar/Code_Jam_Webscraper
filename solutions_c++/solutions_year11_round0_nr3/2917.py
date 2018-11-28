#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <list>
#include <set>
#include <vector>

using namespace std;

int rec(vector<int>& candies, int i, int xs1, int xs2, int s1, int s2)
{
  if(i == candies.size()) return ((xs1^xs2) == 0 && s2)?s1:-1;
  int a = rec(candies, i+1, xs1^candies[i], xs2, s1+candies[i], s2);
  int b = rec(candies, i+1, xs1, xs2^candies[i], s1, s2+candies[i]);
  return max(a,b);
}

int solve(vector<int>& candies) {
  return rec(candies, 0, 0, 0, 0, 0);
}

void handleCase(int casenum) {
  int N;
  cin >> N;
  vector<int> candies;
  for(int i = 0; i < N; ++i) {
    int c;
    cin >> c;
    candies.push_back(c);
  }
  int val = solve(candies);
  cout << "Case #" << casenum << ": ";
  if(val < 0) cout << "NO\n";
  else cout << val << "\n";
}

int main() {
  int cases;
  cin >> cases;
  for(int i = 0; i < cases; ++i) {
    handleCase(i+1);
  }
}
