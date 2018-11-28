#include <fstream>
#include <iostream>
#include <vector>
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
      bool bOn = true;
      unsigned int unSnappers, unSnaps;
      vector<bool> snapper;
      inFile >> unSnappers >> unSnaps;
      for (unsigned int j = 0; j < unSnappers; j++)
      {
        snapper.push_back(false);
      }
      outFile << "Case #" << (i + 1) << ": ";
      for (unsigned int j = 0; j < unSnaps; j++)
      {
        unsigned int unIndex = 0;
        snapper[unIndex] = ((snapper[unIndex])?false:true);
        while (!snapper[unIndex] && ++unIndex < unSnappers)
        {
          snapper[unIndex] = ((snapper[unIndex])?false:true);
        }
      }
      for (unsigned int j = 0; j < unSnappers; j++)
      {
        if (!snapper[j])
        {
          bOn = false;
        }
      }
      outFile << ((bOn)?"ON":"OFF") << endl;
    }
  }
  inFile.close();
  outFile.close();

  return 0;
}
