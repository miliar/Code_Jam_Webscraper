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

int r,c;
char tab[55][55];
int tem[6][6];
struct direc {
  int x, y;
  direc(int x=0, int y=0):x(x),y(y){}
};
direc at[55][55];

void dir(int i, int j, int v)
{
  if(tab[i][j]=='-' && v) at[i][j]=direc(0,1);
  else if(tab[i][j]=='-') at[i][j]=direc(0,-1);
  else if(tab[i][j]=='|' && v) at[i][j]=direc(1,0);
  else if(tab[i][j]=='|') at[i][j]=direc(-1,0);
  else if(tab[i][j]=='\\' && v) at[i][j]=direc(1,1);
  else if(tab[i][j]=='\\') at[i][j]=direc(-1,-1);
  else if(tab[i][j]=='/' && v) at[i][j]=direc(1,-1);
  else if(tab[i][j]=='/') at[i][j]=direc(-1,1);  
}
bool isvalid(int a, int b)
{
  return a>=0 && b>=0 && a<r && b<c;
}
int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d %d",&r,&c);
      for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
	  scanf(" %c",&tab[i][j]);
      
      int saida =0;				
      for(int kk=0;kk<(1<<(r*c));kk++)
	{
	  for(int i=0;i<r;i++)
	    for(int j=0;j<c;j++)
	      tem[i][j]=1,dir(i,j,kk & (1<<(i*c +j)));
	  if(kk==-2)
	    {
	      for(int i=0;i<r;i++)
		{
		  for(int j=0;j<c;j++)
		    printf("<%d %d>",at[i][j].x,at[i][j].y);
		  printf("\n");
		}	    
	    }
	  int ax[6][6];
	  bool ok= true;
	  for(int pp=0;ok&& pp<111;pp++)
	    {
	      memset(ax,0,sizeof(ax));
	      for(int i=0;ok && i<r;i++)
		{
		  for(int j=0;ok && j<c;j++)
		    if(tem[i][j])
		      {
			int x = i+at[i][j].x;
			int y = j+at[i][j].y;
			x = (x+r)%r;
			y=  (y+c)%c;
			if(isvalid(x,y))
			  {
			    ax[x][y]++;
			    if(ax[x][y]>1)ok=false;
			  }
		      }
		}
	      memcpy(tem,ax,sizeof(ax));
	      
	    }
	  
	  if(ok)
	    {
	      saida++;
	      	    
	    }
	}
      printf("Case #%d: %d\n",pp,saida);
    }
  return 0;
}

