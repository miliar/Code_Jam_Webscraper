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

struct Step {
  int number;
  int button;
};

struct Robot {
  list<Step> steps;
  int pos;

  Robot() : pos(1) {}
};

int main(int argc, char **args)
{
  string dir = desktopDir();
  list<string> files;
  if (listFiles(dir, "A-", ".in", &files) == 0)
    return -2;

  for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
  {
    ifstream input((dir + *fileIte).c_str());
    ofstream output((dir + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

    int numCases;
    input >> numCases;
    for (int caseNum = 0; caseNum < numCases; ++ caseNum)
    {
      int numSteps;
      input >> numSteps;
      int result = 0;

      Robot o, b;
      char robot;
      Step step;
      for (int i = 0; i < numSteps; ++i) {
        input >> robot;
        input >> step.button;
        step.number = i;

        (robot == 'O' ? o : b).steps.push_back(step);
      }

      while (!o.steps.empty() || !b.steps.empty()) {
        Robot *curr, *other;

        if (b.steps.empty() || (!o.steps.empty() && o.steps.front().number < b.steps.front().number)) {
          curr = &o; other = &b;
        }
        else {
          curr = &b; other = &o;
        }

        int button = curr->steps.front().button;
        int stepSize = abs(button - curr->pos) + 1;
        curr->pos = button;
        result += stepSize;
        curr->steps.pop_front();

        if (!other->steps.empty()) {
          int delta = other->steps.front().button - other->pos;
          if (abs(delta) <= stepSize)
            other->pos = other->steps.front().button;
          else
            other->pos = other->pos + (delta > 0 ? stepSize : -stepSize);
        }
      }

      stringstream caseResult;
      caseResult << "Case #" << caseNum + 1 << ": " << result;
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
