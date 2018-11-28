#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

// em caso de emergencia
#define _inline(f...) inline f() __attribute__((always_inline)); f
char tab[155][155];
int dirx[8]={-1,-1, 0, 1, 1, 1, 0,-1};
int diry[8]={ 0,-1,-1,-1, 0, 1, 1, 1};
int n,m;
bool ver(char x,int d)
{
  //bool ok=false;
  for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
	{
	  int px=i,py=j,p=0;
	  for(p=0;p<m;p++)
	    {
	      if(px>=n || py>=n || px<0 || py<0)break;
	      if(tab[px][py]!=x)break;
	      px+=dirx[d];
	      py+=diry[d];
	     
	    }
	  //  printf("%d\n" ,p);
	  if(p==m)return true;
	}
    }
  return false;
} 
void rotate()
{
  for(int i=0;i<n;i++)
    {
      for(int kk=0;kk<n;kk++)
      for(int j=n-1;j>0;j--)
	if(tab[i][j]=='.')swap(tab[i][j],tab[i][j-1]);
    }
  
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      printf("Case #%d: ",pp);
      scanf("%d %d",&n,&m);
      for(int i=0;i<n;i++)
	scanf(" %s",tab[i]);
      rotate();
      bool ok1=false,ok2=false;
      
      //for(int i=0;i<n;i++)
      //	printf("%s\n",tab[i]);

      for(int i=0;i<8;i++)
	{
	  if(!ok1)ok1=ver('B',i);
	  if(!ok2)ok2=ver('R',i);
	}
      if(ok1 && ok2)
	printf("Both\n");
      else if(ok1 && !ok2)
	printf("Blue\n");
      else if(!ok1 && ok2)
	printf("Red\n" );
      else if(!ok1 && !ok2)
	printf("Neither\n" );
      else
	printf("mto azar\n" );
    }
  return 0;
}
