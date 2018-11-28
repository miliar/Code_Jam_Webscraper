#include <cstdio>
#include <string>
#include <map>

using namespace std;


struct DirEntry
{
   bool exists;
   map<string, DirEntry > DirTree;

   DirEntry() : exists(0) {}
};

int countdir(DirEntry & dir)
{
   int n = 0;

   for(map<string, DirEntry>::iterator i = dir.DirTree.begin(); i != dir.DirTree.end(); ++i)
   {
      n += countdir(i->second);
   }

   if(!dir.exists)
      ++n;

   return n;
}

int main(void)
{
   int T, t;
   char path[128];

   scanf("%d", &T);

   for(t = 1; t <= T; ++t)
   {
      int N, M;
      DirEntry root;
      root.exists = true;

      scanf("%d%d", &N, &M);

      for(int i = 0; i < N; ++i)
      {
         scanf("%s", path);
         DirEntry * de = &root;

         for(int j = 0; path[j]; )
         {
            int k;
            for(k = j + 1; path[k] && (path[k] != '/'); ++k);

            string dn(path+j+1, k-j-1);

            de = &de->DirTree[dn];
            de->exists = true;

            j = k;
         }
      }
      for(int i = 0; i < M; ++i)
      {
         scanf("%s", path);
         DirEntry * de = &root;

         for(int j = 0; path[j]; )
         {
            int k;
            for(k = j + 1; path[k] && (path[k] != '/'); ++k);

            string dn(path+j+1, k-j-1);

            de = &de->DirTree[dn];

            j = k;
         }
      }

      printf("Case #%d: %d\n", t, countdir(root));
   }

   return 0;
}
