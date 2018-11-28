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
int diam[555][555];
int ent[55][55];
int n;

bool tenta(int x,int y,int tam)
{
  //printf("oi\n");
  int vet[555];
  int guarda[555][2];
  for(int i=0;i<tam;i++)
    for(int j=0;j<tam;j++)
      diam[i][j]=-1;
  
  for(int i=x;i<x+n;i++)
    for(int j=y;j<y+n;j++)
      diam[i][j]=ent[i-x][j-y];
  /*for(int i=0;i<tam;i++)
    {
      for(int j=0;j<tam;j++)
	printf("%d",diam[i][j]);
      printf("\n");
      }*/
  for(int k=0;k<=2*tam-2;k++)//vertical
    {
      int a=0;
      int b=k;
      //int vet[555];
      int qte=0;
      while(b>=0)
	{
	  if(b<tam && a<tam)
	    {
	      guarda[qte][0]=a;
	      guarda[qte][1]=b;
	      vet[qte++]=diam[a][b];
	    }
	  a++;
	  b--;
	}

      for(int i=0;i<qte;i++)
	{
	  int x=guarda[i][0];
	  int y=guarda[i][1];
	  if(vet[i]!=vet[qte-i-1] && vet[i]!=-1 && vet[qte-i-1]!=-1)
	    {return false;}
	  if(vet[i]==-1)
	    diam[x][y]=diam[guarda[qte-i-1][0]][guarda[qte-i-1][1]];
	}
    }

  for(int tipo=0;tipo<2;tipo++)
    {
      for(int i=0;i<tam;i++)//horizontal
	{
	  int qte=0;
	  int a=0;
	  int b=i;
	  if(tipo==1)swap(a,b);
	  while(b<tam && a<tam)
	    {
	      guarda[qte][0]=a;
	      guarda[qte][1]=b;
	      vet[qte++]=diam[a][b];
	      b++;
	      a++;
	    }
	  for(int i=0;i<qte;i++)
	    {
	      
	      
	      int x=guarda[i][0];
	      int y=guarda[i][1];
	      if(vet[i]!=vet[qte-i-1] && vet[i]!=-1 && vet[qte-i-1]!=-1)
		{return false;}
	      if(vet[i]==-1)
		diam[x][y]=diam[guarda[qte-i-1][0]][guarda[qte-i-1][1]];
		  
	    }
	}
    }

  
  return true;
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&n);
      for(int i=1;i<2*n;i++)
	{
	  int bla;
	  if(i<n)
	    {
	      bla=i;
	      int y=n-i;
	      int x=0;
	      for(int j=0;j<bla;j++)
		{
		  scanf("%d",&ent[x][y]);
		  x++;y++;
		}
	    }
	  else
	    {
	      bla=2*n-i;
	      int y=0;
	      int x=i-n;
	      for(int j=0;j<bla;j++)
		{
		  scanf("%d",&ent[x][y]);
		  x++;y++;
		}
	      
	    }
	}
      /*
      for(int i=0;i<n;i++)
	{
	  for(int j=0;j<n;j++)
	    printf("%d ",ent[i][j]);
	  printf("\n");
	  }*/

      int size=n;
      for(size=n;;size++)
	{
	 
	  bool ok=false;
	  for(int i=0;!ok && i<=size-n;i++)
	    for(int j=0;!ok && j<=size-n;j++)
	      ok=tenta(i,j,size);
	 
	  if(ok)break;
	}
      printf("Case #%d: %d\n",pp,size*size-n*n);
      //      return size*size-n*n;
    }
  return 0;
}
