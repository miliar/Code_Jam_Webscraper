#include<stdio.h>
#include<memory.h>

FILE* fi, *fo;

int t;

int val;

int w, h;

int i, j, k;

int v[100][100];
int r[100][100];

int x[] = { 0,-1, 1, 0};
int y[] = {-1, 0, 0, 1};

void solve(int i, int j)
{
 int di = i;
 int dj = j;
 
 for(k = 0; k < 4; k++)
  if(i+y[k]>=0 && i+y[k]<h && j+x[k]>=0 && j+x[k]<w)
   if(v[di][dj] > v[i+y[k]][j+x[k]])
   {
    di = i+y[k];
    dj = j+x[k];
   }
   
 if(i==di && j == dj)
 {
  r[i][j] = val++;
  return;
 }
  
 if(r[di][dj] == -1)
 {
  solve(di, dj);  
 }
 
 r[i][j] = r[di][dj];
 
 
}

int main()
{
 fi = fopen("in.txt", "r");
 fo = fopen("out.txt", "w");
 
 fscanf(fi, "%d", &t);
 
 for(int br = 1; br <= t; br++)
 {
  fprintf(fo, "Case #%d:\n", br);
  
  fscanf(fi, "%d%d", &h, &w);
  
  for(i = 0; i < h; i++)
   for(j = 0; j < w; j++)
   {
    fscanf(fi, "%d", &v[i][j]);
    r[i][j] = -1; 
   } 
  
  val = 0;
  
  for(i = 0; i < h; i++, fputc('\n',fo))
   for(j = 0; j < w; j++)
   {
     if(r[i][j] == -1)
     {
      solve(i, j);
     }
      
     fprintf(fo, "%c " ,r[i][j]+'a');
   }
    
 }
 
 return 0; 
}
