#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef map<string, LPVOID> DirTree;

void FreeDirectory(DirTree *dt)
{
  if(dt != NULL)
  {
    DirTree::iterator itr = dt->begin();

    while(itr != dt->end())
    {
      DirTree * dt2 = (DirTree*) itr->second;
      FreeDirectory(dt2);
      delete dt2;
      itr++; 
    }
  }
}



void InsertDirectory(DirTree *dt, string s, unsigned int & NewDirs)
{
  unsigned int pos1 = 0, pos2 = 0, i;
  vector<string> SubDirs(1000);
  unsigned int SubDirCount = 0;
  DirTree * dtAux = dt;

  pos1 = s.find_first_of('/', pos1);
  while(pos1 < s.length())
  {
    string sx;

    pos1 += 1;
    pos2 = s.find_first_of('/', pos1);  

    SubDirs[SubDirCount++] = s.substr(pos1, pos2 - pos1);
    pos1 = pos2;
  }
  for(i = 0; i < SubDirCount ; ++i)
  {
    DirTree::iterator itr;

    itr = dtAux->find(SubDirs[i]);
    if(itr != dtAux->end())
    {
      dtAux = (DirTree*)itr->second;
    }
    else
    {
      DirTree * riau = new DirTree;
      (*dtAux)[SubDirs[i]] = (LPVOID) riau;
      dtAux = riau;
      NewDirs += 1;
    }
  }
}


int 
main(int argc, const char *argv[])
{
  unsigned int i, t;

  cin >> t;

  for(i = 0; i < t ; ++i)
  {
    unsigned int c, cc, j, Result = 0;
    DirTree t;

    cin >> c;
    cin >> cc;

    for(j = 0 ; j < c; ++j)
    {
      string s;

      cin >> s;
      InsertDirectory(&t, s, Result);
    }

    Result = 0;

    for(j = 0 ; j < cc; ++j)
    {
      string s;

      cin >> s;
      InsertDirectory(&t, s, Result);
    }

    FreeDirectory(&t);

    cout << "Case #" << i+1 << ": " << Result << endl;
  }

  return 0;
}