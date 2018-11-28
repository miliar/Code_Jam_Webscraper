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
  if (listFiles(dir, "B-", ".in", &files) == 0)
    return -2;

  for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
  {
    ifstream input((dir + *fileIte).c_str());
    ofstream output((dir + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

    int numCases;
    input >> numCases;
    for (int caseNum = 0; caseNum < numCases; ++ caseNum)
    {
      list<char> result;

      vector<char *> combineRules(26, NULL);
      vector<char *> opposedRules(26, NULL);
      int present[26];
      memset(present, 0, 26 * sizeof(int));
      for (int i = 0; i < 26; ++i) {
        combineRules[i] = new char[26];
        opposedRules[i] = new char[26];
        for (int j = 0; j < 26; ++j) {
          combineRules[i][j] = 0;
          opposedRules[i][j] = 0;
        }
      }

      int combines;
      char c1, c2, c3;
      input >> combines;
      for (int i = 0; i < combines; ++i) {
        input >> c1;
        input >> c2;
        input >> c3;

        combineRules[c1 - 'A'][c2 - 'A'] = c3;
        combineRules[c2 - 'A'][c1 - 'A'] = c3;
      }

      int opposeds;
      input >> opposeds;
      for (int i = 0; i < opposeds; ++i) {
        input >> c1;
        input >> c2;

        opposedRules[c1 - 'A'][c2 - 'A'] = 1;
        opposedRules[c2 - 'A'][c1 - 'A'] = 1;
      }

      int n;
      input >> n;
      for (int i = 0; i < n; ++i) {
        input >> c1;

        if (result.empty()) {
          ++present[c1 - 'A'];
          result.push_back(c1);
        }
        else {
          int combination = combineRules[c1 - 'A'][result.back() - 'A'];
          if (combination != 0) {
            --present[result.back() - 'A'];
            result.back() = combination;
            --present[combination - 'A'];
          }
          else {
            bool cleared = false;
            for (int i = 0; i < 26; ++i) {
              if (opposedRules[c1 - 'A'][i] && present[i] > 0) {
                result.clear();
                memset(present, 0, 26 * sizeof(int));
                cleared = true;
              }
            }

            if (!cleared) {
              result.push_back(c1);
              ++present[c1 - 'A'];
            }
          }
        }
      }

      for (int i = 0; i < 26; ++i) {
        delete[] combineRules[i];
        delete[] opposedRules[i];
      }

      stringstream caseResult;
      caseResult << "Case #" << caseNum + 1 << ": [";
      for (list<char>::iterator ite = result.begin(); ite != result.end(); ++ite)
        if (ite == result.begin())
          caseResult << *ite;
        else
          caseResult << ", " << *ite;
      caseResult << "]";
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
