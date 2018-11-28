
#include <list>
#include <algorithm>

#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

FILE *fi;		// input file
FILE *fo; 		// output file

int cases;		// number of cases
int cas; 		// actual case

long long lut[256];

char numstr[50];

long long num;

int base;

int main(int argc,char **argv)
{
 if (argc!=2) { printf("Nincs input!\n"); return 0; }
 fi = fopen(argv[1],"r");
 fo = fopen("output.file","w");

 fscanf(fi,"%d",&cases);

 for (cas=1; cas<=cases; cas++)
 {
  // ------------------------------------------------------------------------------
  fscanf(fi,"%s",numstr);

  base = 0;
  for (int i=0; i<256; i++) lut[i] = -1;
  for (int i=0; i<(int)strlen(numstr); i++)
   if (lut[(int)numstr[i]] == -1) lut[(int)numstr[i]] = base++;

  for (int i=0; i<256; i++)
  {
   if (lut[i]==0) lut[i]=1;
   else
   if (lut[i]==1) lut[i]=0;

   if(lut[i]!=-1) printf("%c = %d\n",i,lut[i]);
  }

  if (base == 1) base++;

  num = 0;
  for (int i=0; i<(int)strlen(numstr); i++)
  {
   num = num * base + lut[(int)numstr[i]];
  }

  printf("%s, %lld, %d\n",numstr,num,base);

  fprintf(fo,"Case #%d: %lld\n",cas,num);
  // ------------------------------------------------------------------------------
 }

 fclose(fi);
 fclose(fo);
 return 0;
}


