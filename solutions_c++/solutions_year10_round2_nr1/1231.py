#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

#define forn(i, n) for(int i=0;i<(n);i++)
#define fornr(i, n) for(int i=(n)-1; i>=0; i--)
#define ffo find_first_of

set<string> paths;
char dir[101];
vector< set<string>* > depth;

int main(int argc, char *argv[])
{
   int N, M, T;

   cin >> T;

   forn(c, T)
   {
      cin >> N >> M;
      string path, dir;
      set<string>* ptr;
      bool go_on;
      unsigned int d, sz, lpos, pos;
      int res=0;

      forn(i, N)
      {
         cin >> path;
         sz = path.size();
         lpos = 1;
         pos = 0;
         d = 0;
         while(pos<sz)
         {
            if(d==depth.size())
            {
               ptr = new set<string>;
               depth.push_back(ptr);
            }

            pos = path.ffo('/', lpos);
            dir = path.substr(0, min(pos, sz));
            depth[d++]->insert(dir);
            lpos = pos+1;
         }
      }

      forn(j, M)
      {
         cin >> path;
         lpos = 1;
         pos = 0;
         d=0;
         sz=path.size();
         while(pos < sz)
         {
             if(d==depth.size())
            {
               ptr = new set<string>;
               depth.push_back(ptr);
            }

            pos = path.ffo('/', lpos);
            dir = path.substr(0, min(pos, sz));

            if(depth[d]->find(dir)==depth[d]->end())
            {
               depth[d]->insert(dir);
               res++;
            }
            d++;
            lpos = pos+1;
         }
      }
      cout << "Case #" << c+1 <<": " << res << endl;

      for(int j=0;j<depth.size();j++)
         delete depth[j];
      depth.clear();
   }
   return 0;

}
