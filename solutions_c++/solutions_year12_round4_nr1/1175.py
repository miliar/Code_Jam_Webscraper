#include <cstdio>
#include <algorithm>

#define N 10002

int pos[N], len[N], ispos[N];

void testcase() {
   int n, d;
   scanf("%d", &n);
   for(int i = 0; i < n; i++) {
      ispos[i] = 0;
      scanf("%d %d", &pos[i], &len[i]);
   }
   scanf("%d", &pos[n]);
   len[n] = 0;
   n++;
   
   ispos[0] = pos[0];
   for(int i = 1; i < n; i++) {
      for(int j = 0; j < i; j++) {
         if(ispos[j] && ispos[j] + pos[j] >= pos[i]) {
            //printf("%d >= %d\n", ispos[j] + pos[j], pos[j]);
            ispos[i] = std::max(ispos[i], std::min(pos[i] - pos[j], len[i]));
            //printf("from %d = %d, ispos[%d] = %d\n", ispos[j], j, i, ispos[i]);
            if(i == n-1) { printf("YES"); return; }
         }
      }
   }
   printf("NO");
}

int main() {
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   
   int t; scanf("%d", &t);
   for(int i = 1; i <= t; i++) {
      printf("Case #%d: ", i);
      testcase();
      printf("\n");
   }
}
