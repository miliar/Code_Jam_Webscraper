
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

FILE *fi;		// input file
FILE *fo; 		// output file

int cases;		// number of cases
int cas; 		// actual case


char welcome[] = "welcome to code jam";

char str[600];

int *inta = new int[1];
int s;
int wlen;
int slen;

int check(int w, int p)
{
 if (w==wlen) return 1;
 if (p==slen) return 0;

 int sum = 0;

 for (int i=p; i<slen; i++)
  if (welcome[w] == str[i]) sum += check(w+1,i+1);

 return sum;
}

int main(int argc,char **argv)
{
 wlen = strlen(welcome);
 printf("%d\n",wlen);
 if (argc!=2) { printf("Nincs input!\n"); return 0; }
 fi = fopen(argv[1],"r");
 fo = fopen("output.file","w");

 fscanf(fi,"%d",&cases);
 fgets(str,200,fi);

 for (cas=1; cas<=cases; cas++)
 {
  s = 0;
  // ------------------------------------------------------------------------------
  fgets(str,600,fi);

  slen = strlen(str);

  s = check(0,0);
  printf("%d %d\n",s,slen);

  fprintf(fo,"Case #%d: %04d\n",cas,s%10000);
  // ------------------------------------------------------------------------------
 }

 fclose(fi);
 fclose(fo);
 return 0;
}


