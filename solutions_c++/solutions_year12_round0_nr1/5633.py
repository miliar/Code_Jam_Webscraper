#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

int main(){
   map< char, char > m;
   char c, k;
   int n;
   FILE *di = fopen("di.in", "r");
   m['a'] = 'y';
   for (int i = 0; i!=24; i++){
      fscanf(di, "%c", &c);
      m[c] = 'a'+i;
   }
   m['q'] = 'z';
   m[' '] = ' ' ;
   FILE *fi = fopen("in.in", "r");
   fscanf(fi, "%d\n", &n);
   FILE *fo = fopen("out.out", "w");
   for (int i = 0; i!=n; i++){
      fprintf(fo, "Case #%d: ", i+1);
      fscanf(fi, "%c", &c);
      while(c!='\n'){ 
         fprintf(fo, "%c", m[c]);
         fscanf(fi, "%c", &c);
      }
      fprintf(fo, "\n");
   }
   //system("pause");
}
