#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

int milk[10][100]; //N,M


int main()
{
  int i,j,k,n; int C,c;

  scanf("%d",&C);
  for(c=1;c<=C;c++)
  {
    memset(milk,0,sizeof(milk));
    int N,M,T,X,Y;
    scanf("%d %d",&N,&M);
    for(j=0;j<M;j++)
    {
      scanf("%d",&T);
      for(i=0;i<T;i++)
      {
        scanf("%d %d",&X,&Y);
        X--;
        milk[X][j]=2+Y;
      }
    }

//for(j=0;j<3;j++){for(i=0;i<5;i++) printf("%d ",milk[j][i]); printf("\n"); }

    int best=-1; int bestmalts=1000000;
    for(int s=0;s<(1<<N);s++)
    {
//printf("%d\n",s);
      int numalts=__builtin_popcount(s);  bool iederblij=true;
      for(j=0;j<M;j++)
      {
        bool hijblij=false;
        for(i=0;i<N;i++)
          if(milk[i][j]) //als het hem interesseert
          {
//printf("[%d][%d]\n",milk[i][j]&1,((s>>i)&1));
            if((milk[i][j]&1)==((s>>i)&1))
              hijblij=true;
          }
//if(hijblij) printf("ja\n"); else printf("nee\n");
        if(!hijblij) iederblij=false;
      }

      if(iederblij&&numalts<bestmalts)
      { best=s; bestmalts=numalts; }
    }


    printf("Case #%d:",c);
    if(bestmalts==1000000)
      printf(" IMPOSSIBLE\n");
    else
    {
      for(j=0;j<N;j++)
        printf(" %c",(best&(1<<j))?'1':'0');
      printf("\n");
    }
  }
  
  return 0;
}

