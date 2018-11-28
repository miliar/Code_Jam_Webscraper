#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream fin("B-large.in");
  ofstream fout("output.txt");

  int test_cases;
  fin >> test_cases;

  for (int round = 1; round <= test_cases; ++round) {
    int n, s, p;
    int result = 0;
    fin >> n >> s >> p;
    for (int i = 0; i < n; ++i) {
      int sum;
      fin >> sum;
      if (sum % 3 == 0 && sum / 3 >= p)
        result++;
      else if (sum % 3 != 0 && sum / 3 + 1 >= p)
        result++;
      else if (s > 0 && sum / 3 + sum % 3 >= p) {
        s--;
        result++;
      }
      else if (s > 0 && sum % 3 == 0 && sum / 3 == p - 1 && sum / 3 - 1 >= 0) {
        s--;
        result++;
      }
    }

    fout << "Case #" << round << ": " << result << endl;
  }
  fin.close();
  fout.close();
}
