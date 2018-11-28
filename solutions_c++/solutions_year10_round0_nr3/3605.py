#include <fstream>
#include <iostream>
#include <list>
using namespace std;

int main()
{
  ifstream inFile("data/in.dat");
  ofstream outFile("data/out.dat");

  if (inFile.good() && outFile.good())
  {
    unsigned int unTests;
    inFile >> unTests;
    for (unsigned int i = 0; i < unTests; i++)
    {
      unsigned int unRides, unMax, unGroups, unProfit = 0;
      list<unsigned int> queue;
      inFile >> unRides >> unMax >> unGroups;
      for (unsigned int j = 0; j < unGroups; j++)
      {
        unsigned int unPeople;
        inFile >> unPeople;
        queue.push_back(unPeople);
      }
      outFile << "Case #" << (i + 1) << ": ";
      for (unsigned int j = 0; j < unRides; j++)
      {
        bool bFull = false;
        unsigned int unCount = 0;
        list<unsigned int> riding;
        while (!bFull && !queue.empty())
        {
          if (queue.front() + unCount <= unMax)
          {
            unCount += queue.front();
            unProfit += queue.front();
            riding.push_back(queue.front());
            queue.pop_front();
          }
          else
          {
            bFull = true;
          }
        }
        for (list<unsigned int>::iterator k = riding.begin(); k != riding.end(); k++)
        {
          queue.push_back(*k);
        }
        riding.clear();
      }
      outFile << unProfit << endl;
    }
  }
  inFile.close();
  outFile.close();

  return 0;
}
