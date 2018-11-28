
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

FILE *fi;		// input file
FILE *fo; 		// output file

int cases;		// number of cases
int cas; 		// actual case

char chara[1];

int inta[1];

int map[100][100];
int cmap[100][100];

int r,c;

char next;

void flow(int i, int j)
{
 int a=-1;
 int b=-1;
 int h=map[i][j];
 char low;
 char high;

 // North
 if (i>0 && map[i-1][j]<h)
 {
  h = map[i-1][j];
  a = i-1;
  b = j;
 }


 // West
 if (j>0 && map[i][j-1]<h)
 {
  h = map[i][j-1];
  a = i;
  b = j-1;
 }


 // East
 if (j<c-1 && map[i][j+1]<h)
 {
  h = map[i][j+1];
  a = i;
  b = j+1;
 }


 // South
 if (i<r-1 && map[i+1][j]<h)
 {
  h = map[i+1][j];
  a = i+1;
  b = j;
 }

 if (a==-1) { if(cmap[i][j] == 0) {cmap[i][j] = next; next++; } }
 else
 {
  if (cmap[a][b]==0 && cmap[i][j]==0) 
  {
   cmap[i][j] = next;
   cmap[a][b] = next;
   next++;
  }
  else if (cmap[a][b]!=0 && cmap[i][j]==0)
  {
   cmap[i][j] = cmap[a][b];
  }
  else if (cmap[a][b]==0 && cmap[i][j]!=0)
  {
   cmap[a][b] = cmap[i][j];
  }
  else if (cmap[a][b] != cmap[i][j])
  {
   low = (cmap[i][j]<cmap[a][b]?cmap[i][j]:cmap[a][b]);
   high = (cmap[i][j]>cmap[a][b]?cmap[i][j]:cmap[a][b]);

   for (int t1=0;t1<r;t1++)
    for (int t2=0;t2<c;t2++)
    {
     if (cmap[t1][t2] == high) cmap[t1][t2] = low;
     if (cmap[t1][t2] > high) cmap[t1][t2]--;
    }

   next--;
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
  next = 1;
  // ------------------------------------------------------------------------------
  fscanf(fi,"%d %d",&r,&c);
  for (int i=0;i<r;i++)
   for (int j=0; j<c; j++)
   {
    fscanf(fi,"%d",&map[i][j]);
   }

  for (int i=0;i<100;i++)
   for (int j=0; j<100; j++) cmap[i][j] = 0;

  for (int i=0;i<r;i++)
   for (int j=0; j<c; j++) 
   {
    flow(i,j);
    
   }

  fprintf(fo,"Case #%d:\n",cas);
  for (int i=0; i<r; i++)
  {
   for (int j=0; j<c; j++)
   {
    fprintf(fo,"%c",cmap[i][j]+'a'-1);
    if (j<c-1) fprintf(fo," ");
   }
   fprintf(fo,"\n");
  }

  // ------------------------------------------------------------------------------
 }

 fclose(fi);
 fclose(fo);
 return 0;
}


