#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
  int nTests;
  ifstream inFile(argv[1]);

  inFile >> nTests;
  for (int i = 0; i < nTests; i++)
  {
    bool bFound = false;
    unsigned long long ullPossibleGamesToday;
    unsigned int unPercentageToday, unPercentageTotal;
    inFile >> ullPossibleGamesToday >> unPercentageToday >> unPercentageTotal;

    for (unsigned long long j = 1; !bFound && j <= ullPossibleGamesToday; j++)
    { 
      for (unsigned long long k = 0; !bFound && k <= j; k++)
      { 
        if ((k * 100) % j == 0 && (k * 100) / j == unPercentageToday && (unPercentageToday == unPercentageTotal || (unPercentageToday > 0 && unPercentageTotal > 0 && unPercentageTotal != 100)))
        { 
          bFound = true;
        } 
      } 
    }
/*
    if (unPercentageToday == unPercentageTotal || (unPercentageToday > 0 && unPercentageTotal > 0 && unPercentageTotal != 100))
    {
      for (unsigned long long j = 1; !bFound && j <= ullPossibleGamesToday; j++)
      {
        for (unsigned long long k = 0; !bFound && k <= j; k++)
        {
          if ((k * 100) % j == 0 && (k * 100) / j == unPercentageToday && (unPercentageToday == unPercentageTotal || (unPercentageToday > 0 && unPercentageTotal > 0 && unPercentageTotal != 100)))
          {
            bFound = true;
          }
        }
      }
    }
*/
    cout << "Case #" << (i + 1) << ": " << ((bFound)?"Possible":"Broken") << endl;
  }
  inFile.close();

  return 0;
}
