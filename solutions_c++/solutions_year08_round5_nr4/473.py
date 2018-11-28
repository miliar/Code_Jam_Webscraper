#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 101

bool rock[MAX][MAX];
long long T[MAX][MAX];
bool v[MAX][MAX];
int H,R,W;

long long nways(int r, int c)
{
    long long res;
    if(r==H&&c==W)
                  return 1;
    if(r>H||c>W||rock[r][c]) return 0;
    if(v[r][c]) return T[r][c];
    res = ((nways(r+2,c+1))+(nways(r+1,c+2)));
    v[r][c]=true;
    return T[r][c]=res;
}

main()
{
      int t,nc=1;
      int r,c;
      FILE *in = fopen("D-small-attempt3.in","r");
      FILE *out = fopen("D-small.out","w");
      
      //FILE *in = fopen("D-large.in","r");
      //FILE *out = fopen("D-large.out","w");
      
      fscanf(in,"%d",&t);
      while(t--)
      {
             printf("%d\n",t);
             memset(v,false,sizeof(v));
             memset(rock,false,sizeof(rock));   
             fscanf(in,"%d %d %d",&H,&W,&R);
             for(int i=0;i<R;i++)
             {
                     fscanf(in,"%d %d",&r,&c);
                     rock[r][c]=true;
             }
             fprintf(out,"Case #%d: ",nc++);
             
             //Algorithm-begins
             fprintf(out,"%I64d",nways(1,1)%(long long)10007);
             //Algorithm-ends             
             
             fprintf(out,"\n");
      }
      system("PAUSE");
      fclose(out);
      return 0;
}
