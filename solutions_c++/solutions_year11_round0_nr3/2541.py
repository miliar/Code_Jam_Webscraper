#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define WIN32_LEAN_AND_MEAN
#undef UNICODE
#include <windows.h>

string desktopDir();
size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files);

int main(int argc, char **args)
{
  string dir = desktopDir();
  list<string> files;
  if (listFiles(dir, "C-", ".in", &files) == 0)
    return -2;

  for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
  {
    ifstream input((dir + *fileIte).c_str());
    ofstream output((dir + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

    int numCases;
    input >> numCases;
    for (int caseNum = 0; caseNum < numCases; ++ caseNum)
    {
      int numCandies;
      input >> numCandies;

      
      
      long minCandy;
      input >> minCandy;
      long impossible = minCandy;
      long seansPile = 0;
      long candy;
      for (int i = 1; i < numCandies; ++i) {
        input >> candy;
        impossible ^= candy;

        if (candy < minCandy) {
          seansPile += minCandy;
          minCandy = candy;
        }
        else
          seansPile += candy;
      }

      stringstream caseResult;
      caseResult << "Case #" << caseNum + 1 << ": ";
      if (impossible)
        caseResult << "NO";
      else
        caseResult << seansPile;
      output << caseResult.str() << endl;
      cout << caseResult.str() << endl;
    }
  }
  
  return 0;
}

string desktopDir()
{
  char buffer[MAX_PATH];
  GetEnvironmentVariable("USERPROFILE", buffer, MAX_PATH);
  return string(buffer) + "\\Desktop\\";
}

size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files)
{
  files->clear();

  string fileMask = dir + "\\" + prefix + "*" + sufix;
  WIN32_FIND_DATA info;
  HANDLE hFind = FindFirstFile(fileMask.c_str(), &info);
  if (hFind != INVALID_HANDLE_VALUE)
  {
    do
    {
      if (strlen(info.cFileName) > 0)
        files->push_back(info.cFileName);
    } while (FindNextFile(hFind, &info));

    FindClose(hFind);
  }

  return files->size();
}
