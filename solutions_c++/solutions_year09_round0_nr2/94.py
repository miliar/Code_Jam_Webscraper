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
int mov[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
struct ponto
{
  int x;
  int y;
};
int mapa[555][555];
char saida[555][555];
int foi[300];
ponto sink[555][555];
int n,m;
ponto fsink(int a,int b)
{
  if(mapa[a][b]==inf)
    {
      ponto ret;
      ret.x=-1;
      return ret;
    }
  if(sink[a][b].x==-1)
    {
      ponto ret;
      int mn=inf;
      int pp=-1;
      for(int i=0;i<4;i++)
	{
	  int at=mapa[a+mov[i][0]][b+mov[i][1]];
	  if(at<mapa[a][b] && at<mn)
	    {
	      mn=at;
	      pp=i;
	    } 
	}
      if(pp==-1)
	{
	  ret.x=a;
	  ret.y=b;
	}
      else
	ret=fsink(a+mov[pp][0],b+mov[pp][1]);
      sink[a][b]=ret;
    }
  return sink[a][b];
}

int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d %d",&n,&m);
      for(int i=0;i<=n+5;i++)
	for(int j=0;j<=m+5;j++)
	  mapa[i][j]=inf;
     
      for(int i=1;i<=n;i++)
	for(int j=1;j<=m;j++)
	  scanf("%d" ,&mapa[i][j]);
     
      //clear
      for(int i=0;i<n+5;i++)
	 for(int j=0;j<m+5;j++)
	    sink[i][j].x=saida[i][j]=-1;
	  
      for(int i=0;i<300;i++)
	foi[i]=0;
      //find
      for(int i=1;i<=n;i++)
	for(int j=1;j<=m;j++)
	  fsink(i,j);
    
      //teste
/*
      for(int i=1;i<=n;i++)
	{	
	  for(int j=1;j<=m;j++)
	    { 
	      ponto aux=fsink(i,j);
	      printf("<%d-%d>",aux.x,aux.y);
	    }	  
	  printf("\n");
	  }*/    
      
      //end
      int qte=-1;
      printf("Case #%d:\n",pp);
      for(int i=1;i<=n;i++)
	{
	  int a,b;
	  char c;
	  a=fsink(i,1).x;
	  b=fsink(i,1).y;
	  // printf("<%d %d>",a,b);
	  if(saida[a][b]==-1)
	    {
	      qte++;
	      saida[a][b]=qte;
	    }
	  c='a'+saida[a][b];
	  printf("%c",c);
	  for(int j=2;j<=m;j++)
	    {
	      a=fsink(i,j).x;
	      b=fsink(i,j).y;
	      if(saida[a][b]==-1)
		{
		  qte++;
		  saida[a][b]=qte;
		}
	      c='a'+saida[a][b];
	      printf(" %c",c);
	    }
	  printf("\n");
	}
     
    }
  return 0;
}
