#include<stdio.h>
int main()
{
 int T, N, S, p, t;
 int i,j, count, surprise;
 FILE *fin, *fout;

 fin = fopen("input.txt", "r");
 fout= fopen("output.txt", "w");

 fscanf(fin, "%d", &T);

 for (i = 0;i < T;i++)
 {
  fscanf(fin, "%d", &N);
  fscanf(fin, "%d", &S);
  fscanf(fin, "%d", &p);
  
  count = 0;
  surprise = S;
  printf("Case #%d:\n", i);
  for (j = 0;j < N;j++)
  {
   fscanf(fin, "%d", &t);
   int mod = t%3;
   int div = t/3;
   printf("t=%d, lim=%d, mod=%d, div=%d\n", t, p, mod, div);
   switch (mod)
   {
    case 0:
     if (div >= p) count++;
     else if ((div + 1 == p) && surprise>0 && t>0) 
     {
      count++;
      surprise--;
     }
     break;
    case 1:
     if (div + 1 >= p) count++;
     break;
    case 2:
     if (div + 1 >= p) count++;
     else if ((div + 2 == p) && surprise>0 && t>2)
     {
      count++;
      surprise--;
     }
     break;
   }
  }
  fprintf(fout, "Case #%d: %d\n",i+1, count); 
 }
 fclose(fin);
 fclose(fout);
 return 0;
}
