#include <algorithm>
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

size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files);

struct Dir
{
  Dir(const string &name = string())
  {
    this->name = name;
  }

  bool operator ==(const string &dir)
  {
    return name == dir;
  }

  size_t mkdir(const char *dir)
  {
    if (name == dir)
      return 0;

    const char *innerDirFull = &dir[name.length() + 1];
    string innerDir = innerDirFull;
    size_t slash = innerDir.find('/');
    if (slash != string::npos)
      innerDir.resize(slash);

    list<Dir>::iterator ite = find(children.begin(), children.end(), innerDir);
    if (ite == children.end())
    {
      children.push_back(Dir(innerDir));
      return 1 + children.back().mkdir(innerDirFull);
    }
    else
      return ite->mkdir(innerDirFull);
  }

  string name;
  list<Dir> children;
};

int main(int argc, char **args)
{
  if (argc == 1)
    return -1;

  string dir = args[1];
  list<string> files;
  if (listFiles(dir, "A-", ".in", &files) == 0)
    return -2;

  for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
  {
    ifstream input((dir + '/' + *fileIte).c_str());
    ofstream output((dir + '/' + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

    int numCases;
    input >> numCases;
    for (int caseNum = 0; caseNum < numCases; ++ caseNum)
    {
      int n, m;
      input >> n;
      input >> m;
      
      Dir root;
      string dir;
      for (int i = n; --i >= 0;)
      {
        input >> dir;
        root.mkdir(dir.c_str());
      }

      long result = 0;
      for (int i = m; --i >= 0;)
      {
        input >> dir;
        result += root.mkdir(dir.c_str());
      }

      stringstream caseResult;
      caseResult << "Case #" << caseNum + 1 << ": " << result;
      output << caseResult.str() << endl;
      cout << caseResult.str() << endl;
    }
  }
  
  return 0;
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
