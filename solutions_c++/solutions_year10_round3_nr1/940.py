#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Point {
public:
  Point(int p_a, int p_b) {
    a = p_a, b = p_b;
  }

  bool operator<(const Point &p) const {
    if(a < p.a)
      return true;

    if(a > p.a)
      return false;

    return (b < p.b);
  }

  bool intersect(const Point &p) {
    if(a < p.a && b > p.b)
      return true;

    if(a > p.a && b < p.b)
      return true;

    return false;
  }

  int a, b;
};

unsigned long int dostuff(vector<Point> &vec) {
  unsigned long int total = 0;

  for(unsigned int i = 0; i < vec.size(); ++i)
    for(unsigned int j = i+1; j < vec.size(); ++j)
      if(vec[i].intersect(vec[j]))
        ++total;
    
  return total;
}


int main() {
  int n, t, a, b;

  cin >> t;

  for(int i = 0; i < t; ++i) {
    vector<Point> vec;

    cout << "Case #" << (i+1) << ": ";

    cin >> n;

    for(int j = 0; j < n; ++j) {
      cin >> a >> b;

      vec.push_back(Point(a, b));
    }

    sort(vec.begin(), vec.end());

    cout << dostuff(vec) << endl;
  }

  return 0;
}