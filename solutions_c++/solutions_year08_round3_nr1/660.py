#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  int N;
  cin >> N;

  for (int i=1; i<=N; ++i) {
    int P, K, L;
    cin >> P >> K >> L;

    vector<int> f(L); // Frequency distribution for the letters
    for (int j=0; j<L; ++j) {
      cin >> f[j];
    }
    sort(f.begin(), f.end());
    reverse(f.begin(), f.end());

    int result=0;
    for (int j=0; j<L; ++j) {
      result += f[j] * (j/K + 1);
    }

    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}
