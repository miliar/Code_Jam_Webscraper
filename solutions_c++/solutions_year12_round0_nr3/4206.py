#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);

  if (inFile.good())
  {
    int nCases;
    inFile >> nCases;
    for (int i = 0; i < nCases; i++)
    {
      int nA, nB, nFound = 0;;
      inFile >> nA >> nB;
      for (int j = nA; j <= nB; j++)
      {
        int nDigits;
        string strNum;
        stringstream ssNum;
        ssNum << j;
        strNum = ssNum.str();
        nDigits = strNum.size();
        do
        {
          for (int k = nA; k <= nB; k++)
          {
            if (j != k)
            {
              stringstream ssComp;
              ssComp << k;
              if (strNum == ssComp.str())
              {
                nFound++;
              }
            }
          }
          strNum += strNum[0];
          strNum.erase(0, 1);
        } while (strNum != ssNum.str());
      }
      if (nFound % 2 == 1)
      {
        nFound++;
      }
      nFound /= 2;
      cout << "Case #" << (i + 1) << ": " << nFound << endl;
    }
  }
  inFile.close();

  return 0;
}
