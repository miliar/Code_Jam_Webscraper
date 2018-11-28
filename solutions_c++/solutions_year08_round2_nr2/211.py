#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 1001

int PARENT[MAX];
int RANK[MAX];

int MakeSet()
{
    for(int i=0;i<MAX;i++)
    {
            PARENT[i] = i;
            RANK[i] = 0;
    }
}


int Find(int x)
{
     if(PARENT[x] == x)
        return x;
     else
        PARENT[x] = Find(PARENT[x]);
     return PARENT[x];
}

void Union(int x, int y)
{
     int xRoot = Find(x);
     int yRoot = Find(y);
     if(RANK[xRoot] > RANK[yRoot])
         PARENT[yRoot] = xRoot;
     else if(RANK[xRoot] < RANK[yRoot])
         PARENT[xRoot] = yRoot;
     else if(xRoot != yRoot)
     {
         PARENT[yRoot] = xRoot;
         RANK[xRoot]++;
     }
}


main()
{
      int n,T,nc=1,r,A,B,P;
      bool p[1001];
      memset(p,true,sizeof(p));
      vector<int> primos;
      int v[1001];
      for(int i=2;i<1001;i++)
              if(p[i])
              {
                       primos.push_back(i);
                       for(int j=2*i;j<1001;j+=i)
                               p[j]=false;
              }
      for(int i=0;i<primos.size();i++) printf("%d ",primos[i]);
      //system("PAUSE");
      FILE *in = fopen("B-small-attempt1.in","r");
      FILE *out = fopen("B-small.out","w");
      //FILE *in = fopen("A-large.in","r");
      //FILE *out = fopen("A-large.out","w");
      fscanf(in,"%d",&T);
      while(T--)
      {
             printf("%d\n",T);
             fscanf(in,"%d %d %d",&A,&B,&P);
             r = B-A+1;
             MakeSet();
             for(int i=A;i<=B;i++)
                     for(int j=A+1;j<=B;j++)
                     {
                             if(Find(i)==Find(j)) continue;
                             //printf("%d %d\n",i,j);
                             bool si = false;
                             for(int k=primos.size()-1;k>=0&&!si&&primos[k]>=P;k--)
                                     if(i%primos[k]==0&&j%primos[k]==0)
                                     {
                                                             Union(i,j);
                                                             si = true;
                                     }
                     }
             memset(v,0,sizeof(v));
             for(int i=A;i<=B;i++)
                     v[Find(i)]=1;
             r=0;
             for(int i=A;i<=B;i++) r+=v[i];
             fprintf(out,"Case #%d: %d\n",nc++,r);
      }
      fclose(out);
      return 0;
}
