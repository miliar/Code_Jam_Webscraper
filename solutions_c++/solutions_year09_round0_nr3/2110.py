#include<stdio.h>
#include<memory.h>
#include<string.h>

FILE* fi, *fo;

char a[] = "welcome to code jam"; //19
int b[19];

int n;

int i, j;

char r[1000];

int main()
{
 fi = fopen("in.txt", "r");
 fo = fopen("out.txt", "w");
 
 fscanf(fi, "%d\n", &n);
 
 for(int br = 1; br <= n; br++)
 {
  memset(b, 0, sizeof(b));
  fgets(r,1000, fi);
  int l = strlen(r);
  for(i = 0; i < l; i++)
  {
   for(j = 18; j >0; j--)
    if(a[j] == r[i])
     b[j] += b[j-1]%10000;
   if(a[0] == r[i])
   {
    b[0]++;
    b[0]%=10000; 
   }
  }
  fprintf(fo, "Case #%d: %04d\n", br, b[18]);
 }
 
 return 0; 
}
