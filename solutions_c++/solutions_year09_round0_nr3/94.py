#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;

char dest[]="welcome to code jam";
int best[5555][55];
char pal[5555];
int n;
int dp(int a,int b)
{
  if(b==18 && pal[a]==dest[b])return 1;
  else if(b==18)return 0;
  if(best[a][b]==-1)
    {
      int ret=0;
      if(pal[a]==dest[b])
	{
	  for(int i=a+1;i<n;i++)
	    ret+=dp(i,b+1);
	}
      best[a][b]=ret%10000;
    }
  return best[a][b];
}
int main ()
{
  int tt;
  scanf("%d ",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      fgets(pal,5555,stdin);
      pal[strlen(pal)-1]=0;
      n = strlen(pal);
      for(int i=0;i<n+5;i++)
	for(int j=0;j<22;j++)
	  best[i][j]=-1;

      for(int i=18;i>=0;i--)
	{
	  for(int j=n;j>=0;j--)
	    dp(j,i);
	}

      int ret=0;
      for(int i=0;i<n;i++)
	ret+=dp(i,0);
      ret%=10000;
      printf("Case #%d: %04d\n",pp,ret);
    }
  return 0;
}
