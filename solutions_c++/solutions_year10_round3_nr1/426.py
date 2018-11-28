#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
  int tests;
  cin >> tests;

  for (int test = 0; test < tests; ++test) {
    int n;
    cin >> n;
    vector<pair<int, int> > segments;
    for (int i = 0; i < n; ++i)
    {
      int x, y;
      cin >> x >> y;
      segments.push_back(make_pair(x, y));
    }

    sort(segments.begin(), segments.end());

    int result = 0;
    for (int i = 0; i < segments.size(); ++i)
      for (int j = i + 1; j < segments.size(); ++j)
        if (segments[i].first < segments[j].first &&
          segments[i].second > segments[j].second ||
          segments[i].first > segments[j].first &&
          segments[i].second < segments[j].second)
          ++result;
    //result *= 2;
    printf("Case #%d: %d\n", test + 1, result);
  }

  return 0; 
}