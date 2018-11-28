#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Vector : public vector<int64_t>
{
public:
  Vector(int n) : vector<int64_t>(n) {}
  int64_t operator*(const Vector& v) {
    int64_t sum = 0;
    for (int i=0; i<size(); ++i) {
      sum += (*this)[i] * v[i];
    }
    return sum;
  }
};


int main(void)
{
  int T; // Number of tests
  cin >> T;

  for (int i=1; i<=T; ++i) {
    int n; // Vector length
    cin >> n;

    // Two vectors to multiply
    Vector v1(n), v2(n);
    int64_t x;
    
    for (int j=0; j<n; ++j) {
      cin >> v1[j];
    }
    for (int j=0; j<n; ++j) {
      cin >> v2[j];
    }

    // Sort the two vectors
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    // Reverse one of the vectors, to minimize the scalar product
    reverse(v2.begin(), v2.end());

    // Print the scalar product
    cout << "Case #" << i << ": " << v1 * v2 << endl;
  }
}
