#include <stdio.h>
#include <string.h>
#include <fstream>>
#include <math.h>



FILE *istream,*ostream;
int i,x,j,w,o,yp,y;
unsigned long int n,k;
char a[51][51];
char b[51][51];

void print()
{
        for(x=0;x<n;x++){
            for(y=0;y<n;y++)
            {
                printf("%c",a[x][y]);
            }
            printf("\n");
            }
 printf("\n");

}

void fd()
{
     for(x=n-1;x>=0;x--)
            for(y=0;y<n;y++){
                yp=x;
    for(int i=x+1;i<n;i++)
    {
        if(a[i][y]=='.') yp=i; else break;
    }
    if (yp!=x){a[yp][y]=a[x][y];
    a[x][y]='.';}
            }

}

int who()

{
    bool Rx=false,Lx=false,Ry=false,Ly=false;
    bool R,L;
    for(x=0;x<n-k+1;x++)
        for(y=0;y<n;y++){
            R=true;L=true;
          for(int i=0;i<k;i++)
          {
              if((a[x+i][y]=='R')&&(R)) ; else R=false;
              if((a[x+i][y]=='B')&&(L)) ; else L=false;
          }
          if (R) Rx=true;
          if (L) Lx=true;
        }
      //  if (Rx) printf("true "); else printf("false ");
      //  if (Lx) printf("true\n"); else printf("false\n");

        for(x=0;x<n;x++)
        for(y=0;y<n-k+1;y++){
            R=true;L=true;
          for(int i=0;i<k;i++)
          {
              if((a[x][y+i]=='R')&&(R)) ; else R=false;
              if((a[x][y+i]=='B')&&(L)) ; else L=false;
          }
          if (R) Ry=true;
          if (L) Ly=true;
        }
      ///  if (Ry) printf("true "); else printf("false ");
       /// if (Ly) printf("true\n"); else printf("false\n");

        bool Rxy=false,Lxy=false,Ryx=false,Lyx=false;
        for(x=0;x<n-k+1;x++)
        for(y=0;y<n-k+1;y++){
            R=true;L=true;
          for(int i=0;i<k;i++)
          {
              if((a[x+i][y+i]=='R')&&(R)) ; else R=false;
              if((a[x+i][y+i]=='B')&&(L)) ; else L=false;
          }
          if (R) Rxy=true;
          if (L) Lxy=true;
        }
      //  if (Rxy) printf("true "); else printf("false ");
       // if (Lxy) printf("true\n"); else printf("false\n");


         for(x=n-1;x>=k-1;x--)
        for(y=0;y<n-k+1;y++){
            R=true;L=true;
          for(int i=0;i<k;i++)
          {
              if((a[x-i][y+i]=='R')&&(R)) ; else R=false;
              if((a[x-i][y+i]=='B')&&(L)) ; else L=false;
          }
          if (R) Ryx=true;
          if (L) Lyx=true;
        }
        //if (Ryx) printf("true "); else printf("false ");
        //if (Lyx) printf("true\n"); else printf("false\n");
//printf("\n");

if ((Rx==true)||(Ry==true)||(Rxy==true)||(Ryx==true)) R=true; else R=false;
if ((Lx)||(Ly)||(Lxy)||(Lyx)) L=true; else L=false;

if(!R&&L) return 0;
if(R&&!L) return 1;
if((R)&&(L)) return 2;
if(!R&&!L) return 3;



}

void rot()
{

        for(x=0;x<n;x++)
            for(y=0;y<n;y++)
            b[y][n-x-1]=a[x][y];

            for(x=0;x<n;x++)
            for(y=0;y<n;y++)
            a[x][y]=b[x][y];
//print();


            fd();
//print();

}

int main()
{
istream=fopen("B-small.in","r");
ostream=fopen("B-small.out","w");


fscanf(istream,"%d\n",&w);
for(j=1;j<=w;j++)
{
fscanf(istream,"%d %d\n",&n,&k);
////
for(x=0;x<n;x++){
for(y=0;y<n;y++){
fscanf(istream,"%c",&a[x][y]);}
fscanf(istream,"\n");
}//
///////////////

rot();
int r=who();
if(r==0) fprintf(ostream,"Case #%d: Blue\n",j);
if(r==1) fprintf(ostream,"Case #%d: Red\n",j);
if(r==2) fprintf(ostream,"Case #%d: Both\n",j);
if(r==3) fprintf(ostream,"Case #%d: Neither\n",j);

}

fclose(istream);
fclose(ostream);

return 0;
}
