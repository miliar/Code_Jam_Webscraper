
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

FILE *fi;		// input file
FILE *fo; 		// output file

int cases;		// number of cases
int cas; 		// actual case

char *chara = new char[1];
char words[5000][50];

char sample[50][50];
char str[500];

int ns[50];

int s;
int l,d;

int state;
int chars;
int subs;

bool check(int x)
{
 int i,j;
 bool res = true;
 bool sub = false;
 for (i=0; i<l; i++)
 {
  sub = false;
  for (j=0; j<ns[i]; j++) 
   if (sample[i][j] == words[x][i]) sub = true;
  if (!sub) res = false;
 }
 return res;
}


int main(int argc,char **argv)
{
 int i,j;

 if (argc!=2) { printf("Nincs input!\n"); return 0; }
 fi = fopen(argv[1],"r");
 fo = fopen("output.file","w");

 fscanf(fi,"%d %d %d",&l,&d,&cases);

 for (i=0;i<d;i++) fscanf(fi,"%s",words[i]);

 for (cas=1; cas<=cases; cas++)
 {
  // ------------------------------------------------------------------------------

  state = 0;
  fscanf(fi,"%s",str);
  chars = 0;
  s = 0;
  for (i=0;i<50;i++) ns[i] = 0;


  for (i=0;i<strlen(str);i++)
  {
   switch (state)
   {
    case 0: 
     if (str[i]=='(') state++; 
     else 
     {
      sample[chars][ns[chars]++] = str[i];
      chars++;
     }
    break;
    case 1:
     if (str[i]==')') { state--; chars++; }
     else
     {
      sample[chars][ns[chars]++] = str[i];
     }
    break;
   }
  }

  for (i=0; i<d; i++)
   if (check(i)) s++;
  

  fprintf(fo,"Case #%d: %d\n",cas,s);
  // ------------------------------------------------------------------------------
 }

 fclose(fi);
 fclose(fo);
 return 0;
}


