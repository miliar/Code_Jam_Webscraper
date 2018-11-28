#include <iostream>
#include <fstream>

#include <set>


using namespace std;


int main() {
  ifstream input("C-small-attempt1.in", ifstream::in);
  ofstream output("problem-c.out", ofstream::out);

  int caseCount;
  input >> caseCount;
  

  for (int caseId = 1; caseId <= caseCount; ++caseId) {
    int a, b;

    input >> a >> b;

    int count = 0;
    
    int digits = ((int)log10(a));
    int multiplier = (int)pow(10, digits);
    
    set<pair<int,int>> ms;

    for (int n = a; n < b; ++n) {
      //transform each n to all possible ms

      int m = n;

      for (int j = 0; j < digits; ++j) {
        //find all recycled numbers m from n and test if a < m <= b
        int lastDigit = m % 10;
        m = m/10 + multiplier * lastDigit;

        if (a < m && m <= b && n != m) {
          ms.insert(make_pair(min(n,m), max(n,m)));
        }
      }
    }

    output << "Case #" << caseId << ": " << ms.size() << endl;
  }

  return 0;
}