#include <iostream>
#include <algorithm>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

using namespace std;

#define MAX 15

char c[MAX][MAX];
int T[MAX][1<<MAX];
int n_tests,test;
int i,j,k,R,C,ok,ans=0,mask,mask2;

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d %d",&R,&C);
    for_to(i,1,R)
    {
      scanf(" %s",c[i]);
    }
    for_to(i,0,(1<<C)-1)
    {
      T[0][i]=0;
    }  
    ans=0;
    for_to(i,1,R)
    {
      for_to(mask,0,(1<<C)-1)
      {
        T[i][mask]=0;
        //check line
        ok=1;
        for_to(j,0,C-2)
        {
          if ((mask & (1<<j)) && (mask & (1<< (j+1))))
          {
            ok=0;
          }
        }
        for_to(j,0,C-1)
        {
          if ((mask & (1<<j)) && c[i][j]=='x')
          {
            ok=0;
          }
        }
        if (ok)
        {
          for_to(mask2,0,(1<<C)-1)
          {
            ok=1;
            for_to(j,0,C-1)
            {
              if (!ok) break;
              if (mask2 & (1<<j))
              {
                if (j>0 && (mask & (1<<(j-1))) )
                {
                  ok=0;
                }
                if (j<C-1 && (mask & (1<<(j+1))))
                {
                  ok=0;
                }
              }
            }
            if (ok) T[i][mask]=max(T[i][mask],__builtin_popcount(mask)+T[i-1][mask2]);
          }
          ans=max(ans,T[i][mask]);
        }
      }
    }
    printf("Case #%d: %d\n",test,ans);
  }
  return 0;
}
