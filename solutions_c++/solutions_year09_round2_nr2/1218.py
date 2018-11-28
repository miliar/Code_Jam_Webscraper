
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

FILE *fi;		// input file
FILE *fo; 		// output file

int cases;		// number of cases
int cas; 		// actual case

char num[100];

int inta[1];

void shift(int x, int y)
{
 for (int i=y; i>x; i--) num[i] = num[i-1];
}

int comp(const void *a, const void *b)
{
 return (*(char *)a) > (*(char *)b);
}

void calc()
{
  for (int i=strlen(num)-2; i>=0; i--)
  {
   char digit;

   for (int j=strlen(num)-1; j>i; j--)
    if (num[j] > num[i])
    {
     digit = num[j];
     shift(i,j);
     num[i] = digit;

     qsort(num+i+1,strlen(num)-i-1,sizeof(char),comp);

     return;
    }
  }


  qsort(num,strlen(num),sizeof(char),comp);
  num[strlen(num)+1]='\0';
  num[strlen(num)] = '0';
  shift(1,strlen(num)-1);
  num[1] = '0';

  if (num[0] == '0')
  {
   for (int i=0; i<strlen(num); i++)
    if (num[i] != '0')
    {
     char digit = num[i];
     shift(0,i);
     num[0] = digit;
     break;
    }
  }
}

int main(int argc,char **argv)
{
 if (argc!=2) { printf("Nincs input!\n"); return 0; }
 fi = fopen(argv[1],"r");
 fo = fopen("output.file","w");

 fscanf(fi,"%d",&cases);

 for (cas=1; cas<=cases; cas++)
 {
  // ------------------------------------------------------------------------------

  fscanf(fi,"%s",num);

  calc();

  fprintf(fo,"Case #%d: %s\n",cas,num);
  // ------------------------------------------------------------------------------
 }

 fclose(fi);
 fclose(fo);
 return 0;
}


