#include <cstdio>
#include <cstdlib>

inline bool isValid(int pd, int q) {
   return (pd * q) == ((pd * q) / 100) * 100;
}

int main() {
   FILE* in = fopen("A-small-attempt1.in","r");
   FILE* out = fopen("cellout.txt","w");
   
   int t;
   fscanf(in, "%d", &t);
   
   for(int i = 0; i < t; i++) {
      int n, pd, pg;
      fscanf(in, "%d %d %d", &n, &pd, &pg);
      
      fprintf(out, "Case #%d: ", i + 1);
      if(pg >= 100) {
         if(pd == 100) {
            fprintf(out, "Possible\n");
            continue;
         } else {
            fprintf(out, "Broken\n");
            continue;
         }
      } else if(pg == 0) {
         if(pd > 0) {
            fprintf(out, "Broken\n");
            continue;
         } else {
            fprintf(out, "Possible\n");
            continue;
         }
      }
      
      bool valid = false;
      for(int j = n; j > 0; j--) {
         if(isValid(pd, j)) {
            fprintf(out, "Possible\n", j);
            valid = true;
            break;
         }
      }
      
      if(!valid) fprintf(out, "Broken\n");
   }
}
