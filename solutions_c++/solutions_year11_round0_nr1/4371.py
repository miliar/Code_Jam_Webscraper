#include <fstream>
#include <iostream>
#include <list>
using namespace std;

struct step
{
  int nPosition;
  int nStep;
};

int main(int argc, char *argv[])
{
  char cBot;
  int nTests, nSteps;
  ifstream inFile(argv[1]);

  inFile >> nTests;
  for (int i = 0; i < nTests; i++)
  {
    int nPos, nPosition[2] = {0, 0}, nSecond = 0, nStep = 0;
    list<step> bot[2];
    inFile >> nSteps;
    for (int j = 0; j < nSteps; j++)
    {
      step tStep;
      inFile >> cBot >> nPos;
      tStep.nPosition = nPos;
      tStep.nStep = j;
      if (cBot == 'B')
      {
        bot[0].push_back(tStep);
      }
      else
      {
        bot[1].push_back(tStep);
      }
    }
    while (!bot[0].empty() || !bot[1].empty())
    {
      bool bUpStep = false;
      for (int j = 0; j < 2; j++)
      {
        if (!bot[j].empty())
        {
          if (nPosition[j] == bot[j].front().nPosition)
          {
            if (bot[j].front().nStep == nStep)
            {
              bUpStep = true;
              bot[j].pop_front();
            }
          }
          else if (nPosition[j] < bot[j].front().nPosition)
          {
            nPosition[j]++;
          }
          else if (nPosition[j] > bot[j].front().nPosition)
          {
            nPosition[j]--;
          }
        }
      }
      if (bUpStep)
      {
        nStep++;
      }
      nSecond++;
    }
    bot[0].clear();
    bot[1].clear();
    cout << "Case #" << i + 1 << ": " << nSecond - 1 << endl;
  }
  inFile.close();

  return 0;
}
