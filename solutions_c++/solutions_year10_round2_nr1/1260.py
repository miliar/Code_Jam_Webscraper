#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
   int t;

   scanf("%d", &t);
   for(int tp = 0; tp < t; ++tp) {
      int N, M;
      vector< pair<string, int> > p;      

      scanf("%d%d", &N, &M);
      for(int i = 0; i < N; ++i) {
         string ts;
         cin >> ts;
         p.push_back(make_pair(ts, 0));
      }

      for(int i = 0; i < M; ++i) {
         string ts;
         cin >> ts;
         p.push_back(make_pair(ts, 1));
      }

      p.push_back(make_pair("/", 0));
      sort(p.begin(), p.end());

      int sol = 0;
      for(int i = 1; i < (int)p.size() ; ++i) {
         if(p[i].second == 0) continue;

         int j;
         for(j = 0; j < (int)p[i-1].first.size() && p[i-1].first[j] == p[i].first[j] ;++j);
         if(j < (int)p[i].first.size()) 
            sol += count(p[i].first.begin()+j, p[i].first.end(), '/') + (p[i].first[j] != '/');
      }

      printf("Case #%d: %d\n", tp+1, sol);
   }

   return 0;
}
