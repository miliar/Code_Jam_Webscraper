#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

long long X[100];
long long Y[100];

main()
{
      long long n,T,nc=1,A,B,C,D,x0,y0,M;
      long long r;
      FILE *in = fopen("A-small-attempt1.in","r");
      FILE *out = fopen("A-small.out","w");
      //FILE *in = fopen("A-large.in","r");
      //FILE *out = fopen("A-large.out","w");
      fscanf(in,"%I64d",&T);
      while(T--)
      {
             fscanf(in,"%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x0,&y0,&M); 
             X[0] = x0;
             Y[0] = y0;
             for(int i = 1 ;i<n;i++)
             {
              X[i] = (A * X[i-1] + B) % M;
              Y[i] = (C * Y[i-1] + D) % M;
             }
             r=0;
             for(int i=0;i<n;i++)
                     for(int j=i+1;j<n;j++)
                             for(int k=j+1;k<n;k++)
                                     if((X[i]+X[j]+X[k])%3==0&&(Y[i]+Y[j]+Y[k])%3==0) r++;
             fprintf(out,"Case #%I64d: %I64d\n",nc++,r);
      }
      system("PAUSE");
      fclose(out);
      return 0;
}
