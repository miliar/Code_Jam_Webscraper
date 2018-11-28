#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
  int nTests;
  ifstream inFile(argv[1]);

  inFile >> nTests;
  for (int i = 0; i < nTests; i++)
  {
    bool bFirst = true;
    int nCombines, nOpposes, nElements;
    vector<vector<char> > opposeVector;
    map<char, vector<char> > combineMap;
    string strCombine, strOppose, strElements, strResult;
    inFile >> nCombines;
    for (int j = 0; j < nCombines; j++)
    {
      vector<char> combine;
      inFile >> strCombine;
      combine.push_back(strCombine[0]);
      combine.push_back(strCombine[1]);
      combineMap.insert(make_pair(strCombine[2], combine));
    }
    inFile >> nOpposes;
    for (int j = 0; j < nOpposes; j++)
    {
      vector<char> oppose;
      inFile >> strOppose;
      oppose.push_back(strOppose[0]);
      oppose.push_back(strOppose[1]);
      opposeVector.push_back(oppose);
    }
    inFile >> nElements >> strElements;
    for (int j = 0; j < nElements; j++)
    {
      bool bDone = false;
      if (strResult.empty())
      {
        strResult += strElements[j];
      }
      else
      {
        for (map<char, vector<char> >::iterator k = combineMap.begin(); !bDone && k != combineMap.end(); k++)
        {
          if ((strResult[strResult.size() - 1] == k->second[0] && strElements[j] == k->second[1]) || (strResult[strResult.size() - 1] == k->second[1] && strElements[j] == k->second[0]))
          {
            bDone = true;
            strResult[strResult.size() - 1] = k->first;
          }
        }
        for (int k = 0; !bDone && k < opposeVector.size(); k++)
        {
          if (strElements[j] == opposeVector[k][0] || strElements[j] == opposeVector[k][1])
          {
            for (int l = 0; !bDone && l < strResult.size(); l++)
            {
              if (strResult[l] != strElements[j] && (strResult[l] == opposeVector[k][0] || strResult[l] == opposeVector[k][1]))
              {
                bDone = true;
                strResult.clear();
              }
            }
          }
        }
        if (!bDone)
        {
          strResult += strElements[j];
        }
      }
    }
    for (map<char, vector<char> >::iterator j = combineMap.begin(); j != combineMap.end(); j++)
    {
      j->second.clear();
    }
    combineMap.clear();
    for (int j = 0; j < opposeVector.size(); j++)
    {
      opposeVector[j].clear();
    }
    opposeVector.clear();
    cout << "Case #" << i + 1 << ": [";
    for (int j = 0; j < strResult.size(); j++)
    {
      if (bFirst)
      {
        bFirst = false;
      }
      else
      {
        cout << ", ";
      }
      cout << strResult[j];
    }
    cout << "]" << endl;
  }
  inFile.close();

  return 0;
}
