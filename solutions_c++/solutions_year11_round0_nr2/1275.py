#include <cstdio>
#include <vector>

using namespace std;

void solve()
{
   char sir[333];
   bool op[128][128] = {0};
   char comb[128][128] = {0};
   vector<char> sol;
   int n;
   scanf("%d", &n);
   while (n--){
      scanf("%s", sir);
      char a = sir[0], b = sir[1];
      comb[a][b] = comb[b][a] = sir[2];
   }
   scanf("%d", &n);
   while (n--){
      scanf("%s", sir);
      char a = sir[0], b = sir[1];
      op[a][b] = op[b][a] = true;
   }
   scanf("%d", &n);
   scanf("%s", sir);
   for (int i=0; i<n; i++){
      char c = sir[i];
      sol.push_back(c);
      bool tryAgain = true, hasCombined = false;
      if (sol.size() >= 2 && tryAgain){
         tryAgain = false;
         int lung = sol.size();
         char a = sol[lung-2], b = sol[lung-1];
         if (comb[a][b]){
            sol[lung-2] = comb[a][b];
            sol.resize(lung-1);
            hasCombined = tryAgain = true;
         }
      }
      int lung = sol.size();
      if (lung >= 2 && !hasCombined){
         char c = sol[lung-1];
         for (int i=0; i<lung-1; i++)
            if (op[c][sol[i]]){
               sol.clear();
               i = lung;
            }
      }
   }
   printf("[");
   for (int i=0; i<(int)sol.size() - 1; i++)
      printf("%c, ", sol[i]);
   if (sol.size())
      printf("%c", sol[sol.size()-1]);
   printf("]\n");
   fflush(stderr);
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int tst;
   scanf("%d", &tst);
   for (int iter = 1; iter <= tst; iter++){
      printf("Case #%d: ", iter);
      solve();
   }
   return 0;
}