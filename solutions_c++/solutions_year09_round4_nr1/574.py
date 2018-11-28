#include <cstdio>

#include <vector>
#include <string>

using namespace std;

int N;

int main(int argc, char* argv[]) {
   char s[100];
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d", &N);
      vector<int> v;
      for (int i = 0; i < N; ++i) {
         scanf("%s", s);
         string str(s);
         size_t p =  str.find_last_of('1');
         v.push_back(p == string::npos ? 0 : p+1);
      // printf("%d: %d\n", i, v[i]);
      }

      int res = 0;
      for (int i = 0; i < N; ++i) {
         int j = i;
         for (j = i; j < N; ++j) {
            if (i+1 >= v[j]) break;
            ++res;
         }
         if (i != j && j < N) {
            int vj = v[j];
            for (int jj = j-1; jj >= i; --jj)
               v[jj+1] = v[jj];
            v[i] = vj;
         }
      }

      printf("Case #%d: %d\n", tc, res);
   }
   
   return 0;
}
