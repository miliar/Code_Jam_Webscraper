#include <cstdio>
#include <cstdlib>

#define MAX_N 200
#define MAX_CHAR 30

int list[MAX_N];
int count;

int main() {
   FILE* in = fopen("B-large.in","r");
   FILE* out = fopen("magout.txt","w");
   
   int t;
   fscanf(in, "%d\n", &t);
   
   for(int i = 0; i < t; i++) {
      int c, d, n;
      fscanf(in, "%d ", &c);
      
      count = 0;
      int combines[MAX_CHAR][MAX_CHAR];
      bool opposes[MAX_CHAR][MAX_CHAR];
      
      for(int xa = 0; xa < MAX_CHAR; xa++) {
         for(int xb = 0; xb < MAX_CHAR; xb++) {
            combines[xa][xb] = 0;
            opposes[xa][xb] = false;
         }
      }
      
      for(int j = 0; j < c; j++) {
         char b1,b2,nb;
         fscanf(in, "%c%c%c ", &b1, &b2, &nb);
         
         printf("%c + %c = %c\n", b1, b2, nb);
         //system("PAUSE");
         
         combines[b1 - 'A'][b2 - 'A'] = nb - 'A';
         combines[b2 - 'A'][b1 - 'A'] = nb - 'A';
      }
      
      fscanf(in, "%d ", &d);
      for(int j = 0; j < d; j++) {
         char b1, b2;
         fscanf(in, "%c%c ", &b1, &b2);
         
         printf("%c + %c = boom\n", b1, b2);
         //system("PAUSE");
         
         opposes[b1 - 'A'][b2 - 'A'] = true;
         opposes[b2 - 'A'][b1 - 'A'] = true;
      }
      
      fscanf(in, "%d ", &n);
      for(int j = 0; j < n; j++) {
         char b;
         fscanf(in, "%c", &b);
         
         int elem = b - 'A';
         
         // 1. append to the list
         list[count] = elem;
         count++;
         
         // 2. check if it combines with the previous
         while(count > 1) {
            int prev = list[count - 2];
            if(combines[prev][elem]) {
               // combine the two
               list[count - 2] = combines[prev][elem];
               count--;
               
               // change the element
               elem = combines[prev][elem];
            } else break;
         }
         
         // 3. check if there's opposing elements
         for(int k = 0; k < count; k++) {
            if(opposes[list[k]][elem]) {
               // clear list
               count = 0;
               break;
            }
         }
      }
      
      fprintf(out, "Case #%d: [", i + 1);
      for(int j = 0; j < count; j++) {
         fprintf(out, "%c", list[j] + 'A');
         if(j < count - 1) {
            fprintf(out, ", ");
         }
      }
      fprintf(out, "]\n");
   }
   
   fclose(in);
   fclose(out);
}
