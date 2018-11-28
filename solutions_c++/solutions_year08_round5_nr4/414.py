#include <iostream>
#include <cstring>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)
#define clr(a,v) memset(a,v,sizeof(a))

using namespace std;

#define MOD 10007
#define MAX 110

int n_tests,test;
int i,j,k;
int H,W,R;
int T[MAX][MAX];
int block[MAX][MAX];

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d %d %d",&H,&W,&R);
    clr(block,0);
    for_to(i,1,R)
    {
      scanf("%d %d",&j,&k);
      block[j][k]=1;
    }
    T[1][1]=1;
    for_to(i,1,H)
    {
      for_to(j,1,W)
      {
        if (i==1 && j==1) continue;
        T[i][j]=0;
        if (block[i][j]) continue;
        if (i>1 && j>2)
        {
          T[i][j]+=T[i-1][j-2];
        }
        if (i>2 && j>1)
        {
          T[i][j]+=T[i-2][j-1];
        }
        T[i][j]=T[i][j]%MOD;
      }
    }
    printf("Case #%d: %d\n",test,T[H][W]);
  }
  return 0;
}
