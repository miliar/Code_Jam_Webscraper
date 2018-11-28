#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
  double dResult[100][3];
  int nTeams, nTests;
  char cSched[100][100];
  string strSchedule;
  ifstream inFile(argv[1]);

  inFile >> nTests;
  for (int i = 0; i < nTests; i++)
  {
    inFile >> nTeams;
    for (int j = 0; j < nTeams; j++)
    {
      int nWin = 0, nTotal = 0;
      inFile >> strSchedule;
      for (int k = 0; k < nTeams; k++)
      {
        cSched[j][k] = strSchedule[k];
        if (strSchedule[k] != '.')
        {
          nTotal++;
          if (strSchedule[k] == '1')
          {
            nWin++;
          }
        }
      }
      dResult[j][0] = (double)nWin / (double)nTotal;
//cout<<"WP("<<j<<") = "<<dResult[j][0]<<endl;
    }
    for (int j = 0; j < nTeams; j++)
    {
      double dTotal = 0;
      int nCount = 0;
      for (int k = 0; k < nTeams; k++)
      {
        if (cSched[j][k] != '.')
        {
          int nWin = 0, nTotal = 0;
          for (int l = 0; l < nTeams; l++)
          {
            if (l != j && cSched[k][l] != '.')
            {
              nTotal++;
              if (cSched[k][l] == '1')
              {
                nWin++;
              }
            }
          }
          dTotal += (double)nWin / (double)nTotal;
          nCount++;
        }
      }
      dResult[j][1] = dTotal / (double)nCount;
//cout<<"OWP("<<j<<") = "<<dResult[j][1]<<endl;
    }
    for (int j = 0; j < nTeams; j++)
    {
      double dTotal = 0;
      int nCount = 0;
      for (int k = 0; k < nTeams; k++)
      {
        if (cSched[j][k] != '.')
        {
          dTotal += dResult[k][1];
          nCount++;
        }
      }
      dResult[j][2] = dTotal / nCount;
//cout<<"OOWP("<<j<<") = "<<dResult[j][2]<<endl;
    }
    cout << "Case #" << (i+1) << ":" << endl;
    for (int j = 0; j < nTeams; j++)
    {
      cout << fixed << setprecision(12) << ((0.25 * dResult[j][0]) + (0.5 * dResult[j][1]) + (0.25 * dResult[j][2])) << endl;
      //cout << fixed << setprecision(12) << ((0.25 * dResult[j][0]) + (0.5 * dResult[j][1]) + (0.25 * dResult[j][2])) << " = (0.25 * " << dResult[j][0] << ") + (0.5 * " << dResult[j][1] << ") + (0.25 + " << dResult[j][2] << ")" << endl;
    }
  }
  inFile.close();

  return 0;
}
