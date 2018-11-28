#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define MAX_N 2000
#define MAX(a,b) (a > b ? a : b)

using namespace std;

int candy[MAX_N];
int n;

bool cmp(int a, int b) {
   return a > b;
}

int main() {
   FILE* in = fopen("C-large.in","r");
   FILE* out = fopen("candyout.txt","w");
   
   int t;
   fscanf(in, "%d", &t);
   
   for(int i = 0; i < t; i++) {
      fscanf(in, "%d", &n);
      
      int num;
      for(int j = 0; j < n; j++) {
         fscanf(in, "%d", &candy[j]);
         if(j == 0) num = candy[0];
         else num ^= candy[j];
      }
      
      fprintf(out, "Case #%d: ", i + 1);
      if(num == 0) {
         // give the last one to patrick :)
         sort(candy, candy + n, cmp);
         int total = 0;
         for(int j = 0; j < n -1; j++) {
            total += candy[j];
         }
         fprintf(out, "%d\n", total);
      } else {
         fprintf(out, "NO\n");
      }
   }
}
