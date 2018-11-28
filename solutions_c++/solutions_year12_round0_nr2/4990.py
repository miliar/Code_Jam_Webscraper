#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct data
{
  bool bSurprise;
  int nScore[3];
  int nSurprise[3];
};

int nGooglers, nSurprises, nBest;
vector<data *> person;

int hunt(int nPerson = 0, int nSurprise = 0);

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);

  if (inFile.good())
  {
    int nCases;
    inFile >> nCases;
    for (int i = 0; i < nCases; i++)
    {
      inFile >> nGooglers >> nSurprises >> nBest;
      for (int j = 0; j < nGooglers; j++)
      {
        int nTotal, nDiv, nMod;
        data *ptData = new data;
        inFile >> nTotal;
        nDiv = nTotal / 3;
        nMod = nTotal % 3;
        ptData->bSurprise = false;
        ptData->nScore[0] = ptData->nSurprise[0] = nDiv;
        ptData->nScore[1] = ptData->nSurprise[1] = nDiv + ((nMod == 2)?1:0);
        ptData->nScore[2] = ptData->nSurprise[2] = nDiv + ((nMod >= 1)?1:0);
        if (nMod == 1)
        {
          ptData->nSurprise[0] -= 1;
          ptData->nSurprise[1] += 1;
          if (ptData->nSurprise[0] >= 0)
          {
            ptData->bSurprise = true;
          }
        }
        else
        {
          ptData->nSurprise[1] -= 1;
          ptData->nSurprise[2] += 1;
          if (ptData->nSurprise[1] >= 0)
          {
            ptData->bSurprise = true;
          }
        }
        person.push_back(ptData);
      }
      cout << "Case #" << (i + 1) << ": " << hunt() << endl;
      for (int j = 0; j < nGooglers; j++)
      {
        delete person[j];
      }
      person.clear();
    }
  }
  inFile.close();

  return 0;
}

int hunt(int nPerson, int nSurprise)
{
  int nFound[2] = {0, 0};

  if (nPerson < nGooglers)
  {
    nFound[0] = hunt(nPerson + 1, nSurprise) + ((person[nPerson]->nScore[2] >= nBest)?1:0);
    if (nSurprise < nSurprises)
    {
      nFound[1] = hunt(nPerson + 1, nSurprise + 1) + ((person[nPerson]->bSurprise && person[nPerson]->nSurprise[2] >= nBest)?1:0);
    }
  }

  return (nFound[0] >= nFound[1])?nFound[0]:nFound[1];
}
