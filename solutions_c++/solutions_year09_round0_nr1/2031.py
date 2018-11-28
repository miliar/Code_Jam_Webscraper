#include<stdio.h>
#include<memory.h>

FILE* fi, *fo;

int n, d, l;

char dict[5000][15];
bool r[15][26];

int i, j, k;

int main()
{
 fi = fopen("in.txt", "r");
 fo = fopen("out.txt", "w");
 
 fscanf(fi, "%d %d %d", &l, &d, &n);
 
 for(i = 0; i < d; i++)
 {
  fscanf(fi,"\n");
  
  for(j = 0; j < l; j++)
   dict[i][j] = fgetc(fi); 
 }
 
 for(i = 0; i < n; i++)
 {
  memset(r, 0, sizeof(r));
  
  int res = 0;
  
  fscanf(fi,"\n");
  
  for(j = 0; j < l; j++)
  {
   char c = fgetc(fi);
   
   if(c == '(')
    while((c=fgetc(fi)) != ')')
    {
     r[j][c-'a'] = true;
    }
   else
    r[j][c-'a'] = true;
  }
  
  for(j = 0; j < d; j++)
  {
   for(k = 0; k < l && r[k][dict[j][k]-'a']; k++);
   if(k==l)
    res++;
  }
  
  fprintf(fo, "Case #%d: %d\n", i+1, res);
 }
 
 return 0;
}
