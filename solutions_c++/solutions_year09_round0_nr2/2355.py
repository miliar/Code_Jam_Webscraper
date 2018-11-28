#include <stdio.h>
#include <vector>
#include <string.h>

struct pos {int x,y;};
struct dir {pos p1,p2;};

int n,h,w;
int alts[100][100];
int dbs[100][100];

dir dirs[100*100];
int dircount;

void replace(int what, int with)
{
    for (int y=0;y<h;y++)
    {
      for (int x=0;x<w;x++)
      {
        if (dbs[x][y]==what)
        {
          dbs[x][y]=with;
        }
      }
    }
}

int main(int argc, char *argv[])
{
  FILE* in=fopen("B-large.in","r");
  FILE* out=fopen("B-large.out","w");

  fscanf(in,"%i",&n);

  for (int i=0;i<n;i++)
  {

    memset(alts,0,100*100*sizeof(int));
    memset(dbs,0,100*100*sizeof(int));
    dircount=0;
    fscanf(in,"%i %i",&h,&w);

    for (int y=0;y<h;y++) //load input
    {
      for (int x=0;x<w;x++)
      {
        fscanf(in,"%i",&alts[x][y]);
      }
    }

    for (int y=0;y<h;y++) //create directions
    {
      for (int x=0;x<w;x++)
      {
        pos min;
        min.x=x; min.y=y;
        dir newdir;
        newdir.p1=min;
        if (y>0 && alts[x][y-1]<alts[min.x][min.y])
          {min.x=x; min.y=y-1;}
        if (x>0 && alts[x-1][y]<alts[min.x][min.y])
          {min.x=x-1; min.y=y;}
        if (x<w-1 && alts[x+1][y]<alts[min.x][min.y])
          {min.x=x+1; min.y=y;}
        if (y<h-1 && alts[x][y+1]<alts[min.x][min.y])
          {min.x=x; min.y=y+1;}

        if (min.x!=x || min.y!=y)
        {
          newdir.p2=min;
          dirs[dircount++]=newdir;
        }
      }
    }

    for (int y=0;y<h;y++) // dummy values
    {
      for (int x=0;x<w;x++)
      {
        dbs[x][y]=-(y*w+x)-1;
      }
    }


    //merge
    for (int d=0;d<dircount;d++)
    {
      replace(dbs[dirs[d].p1.x][dirs[d].p1.y],dbs[dirs[d].p2.x][dirs[d].p2.y]);
    }

    char maxbas='a';
    replace(dbs[0][0],'a');

    for (int y=0;y<h;y++)
    {
      for (int x=0;x<w;x++)
      {
        if (dbs[x][y]<'a') replace(dbs[x][y],++maxbas);
      }
    }

    fprintf(out,"Case #%i:\n",i+1);

    for (int y=0;y<h;y++)
    {
      for (int x=0;x<w;x++)
      {
        fprintf(out,"%c ",(char)dbs[x][y]);
      }
      fprintf(out,"\n");
    }
  }


  fclose (in);
  fclose (out);

}