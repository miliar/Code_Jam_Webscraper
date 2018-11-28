#include <cstdio>
#include <set>
#include <iostream>
#include <string>
using namespace std;

set<string> dirs, newdirs;

void process(char path[], set<string>& s)
{
  int i = 0;
  while (true)
  {
    while (path[i] != '/')
    {
      if (path[i] == 0)
      {
        s.insert(string(path));
        //printf(">>>%s\n", path);
        return;
      }
      i++;
    }
    path[i] = 0;
    s.insert(string(path));
    //printf(">>>%s\n", path);
    path[i] = '/';
    i++;
  }
}

int main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    dirs.clear();
    newdirs.clear();
    int n, m;
    scanf("%d%d\n", &n, &m);
    
    dirs.insert(string(""));
    for (int i = 0; i < n; i++)
    {
      char path[120];
      scanf("%s\n", path);
      process(path, dirs);
    }
    newdirs = dirs;
    for (int i = 0; i < m; i++)
    {
      char path[120];
      scanf("%s\n", path);
      process(path, newdirs);
    }
    printf("Case #%d: %d\n", t, newdirs.size()-dirs.size());
  }

  return 0;
}

