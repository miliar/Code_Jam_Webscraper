#include <iostream>

using namespace std;

inline unsigned int mod(unsigned int a, unsigned int b)
{
  return a - (b * int(a/b));
}

int main()
{
  unsigned int num_cases = 0; // T
  unsigned int num_snappers = 0, num_snaps = 0;

  cin >> num_cases;

  for (unsigned int t = 0; t < num_cases; ++t) {
    cin >> num_snappers >> num_snaps;

    unsigned int result = num_snaps % (1 << num_snappers);
    cout << "Case #" << (t+1) << ": ";
    if (result == ((1 << num_snappers) - 1)) {
      cout << "ON" << endl;
    } else {
      cout << "OFF" << endl;
    }
  }
}
