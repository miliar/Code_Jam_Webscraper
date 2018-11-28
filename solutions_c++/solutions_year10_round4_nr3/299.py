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
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
int tem[555][555];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      int n;
      scanf("%d",&n);
      memset(tem,0,sizeof(tem));
      for(int i=0;i<n;i++)
	{
	  int a,b;
	  int c,d;
	  scanf("%d %d %d %d",&a,&b,&c,&d);
	  for(int i=a;i<=c;i++)
	    for(int j=b;j<=d;j++)
	      tem[i][j]=1;
	}
      int tempo=0;
      int novo[555][555]={0};
      for(tempo=0;;tempo++)
	{
	  for(int i=1;i<=100;i++)
	    {
	      for(int j=1;j<=100;j++)
		{
		 
		 
		    if(tem[i-1][j]==0 && tem[i][j-1]==0)
		      novo[i][j]=0;
		    else if(tem[i-1][j]==1 && tem[i][j-1]==1)
		      novo[i][j]=1;
		    else
		      novo[i][j]=tem[i][j];
		    
		}
	    }
	  bool ok=false;
	  for(int i=0;i<=100;i++)
	    for(int j=0;j<=100;j++)
	      {
		tem[i][j]=novo[i][j];
		if(tem[i][j])ok=true;
	      }	
	  if(!ok)break;
	}
      printf("Case #%d: %d\n",pp,tempo+1);
    }
  return 0;
}
