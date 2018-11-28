#include <iostream>
using namespace std;

int main()
{
  int cases = 0;
  cin >> cases;
  int caseNum = 1;
  while (caseNum <= cases)
  {
    int googlers = 0;
    cin >> googlers;
    int surprises = 0;
    cin >> surprises;
    int targetScore = 0;
    cin >> targetScore;

    int googlersAtTarget = 0;
    int currentScore = 0;
    for (int i = 1; i <= googlers; i++)
    {
      cin >> currentScore;
      if (targetScore < 2)
      {
        if (currentScore >= targetScore)
          googlersAtTarget++;
        continue;
      }
      if (currentScore < (3 * targetScore - 4))
        continue; // currentScore is too small, even for a surprise
      if (currentScore > (3 * targetScore - 3))
      {
        googlersAtTarget++;
        continue;
      }
      if (surprises > 0) // currentScore must be in the "surprises range"
      {
        surprises--;
        googlersAtTarget++;
      }
    } // for loop
    cout << "Case #" << caseNum << ": " << googlersAtTarget << endl;
    caseNum++;
  } // while loop for cases
  return 0;
}
