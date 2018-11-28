#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <math.h>
using namespace std;

int c[3][3];

float dist(int a, int b)
{
      return (sqrt((c[a][1]-c[b][1])*(c[a][1]-c[b][1])+(c[a][0]-c[b][0])*(c[a][0]-c[b][0]))+c[a][2]+c[b][2])/2;
}

int main(void)
{
  int nc=1,N,C;
  float r,min;  

  FILE *in = fopen("D-small-attempt0.in","r");
  FILE *out = fopen("d.out","w");
  fscanf(in,"%d",&C);
  while(C--)
  {
          fscanf(in,"%d",&N);
          for(int i=0;i<N;i++)
                  fscanf(in,"%d %d %d",&c[i][0], &c[i][1], &c[i][2]);
          r = (float)c[0][2];
          if(N==2){
              r >?= (float)c[1][2];}
          if(N>2)
          {
              r >?= (float)c[2][2];
              min = dist(0,1);
              min <?= dist(0,2);
              min <?= dist(1,2);
              r >?= min;
          }
          printf("Case #%d: %f\n",nc,r);
          fprintf(out,"Case #%d: %f\n",nc++,r);
  }
  system("PAUSE");
  return 0;
}
