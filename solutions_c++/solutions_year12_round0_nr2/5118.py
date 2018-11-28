#include <iostream>

using namespace std;

int main()
{
  int test_cases;
  cin >> test_cases;
  for (int i = 1; i <= test_cases; ++i) {
    int googlers, surprising_triplets, minimum, result = 0;
    cin >> googlers;
    cin >> surprising_triplets;
    cin >> minimum;
    for (int j = 0; j < googlers; ++j) {
      int score;
      cin >> score;
      score -= minimum;
      if (minimum - score / 2 == 2 && surprising_triplets > 0) {
        --surprising_triplets;
        ++result;
      }
      else if (score >= 0 && minimum - score / 2 < 2)
        ++result;
    }
    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}
