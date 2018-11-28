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


int r,c,d;
int tab[555][555];
struct acumula {
  huge a,b;
  acumula (huge a=0, huge b=0): a(a), b(b){}
  inline acumula operator + (const acumula &x)
  {
    return acumula(a+x.a,b+x.b);
  }
  inline acumula operator *( huge m)
  {
    return acumula(a*m,b*m);
  }
  inline acumula operator - (const acumula &x)
  {
    return acumula(a-x.a,b-x.b);
  }
  inline bool operator ==(const acumula &x){
    return a==x.a && b==x.b;
  }
  void print() {
    printf("%lld %lld\n",a,b);
  }
};
acumula acc[555][555];
huge soma[555][555];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d %d %d",&r,&c,&d);
      for(int i=1;i<=r;i++)
	for(int j=1;j<=c;j++)
	  {
	    char c;
	    scanf(" %c",&c);
	    tab[i][j]=d+c-'0';
	  }      
      for(int i=1;i<=r;i++)
	{
	  for(int j=1;j<=c;j++)
	    {
	      acc[i][j] = acc[i-1][j-1];
	      soma[i][j] = soma[i-1][j-1];
	      for(int p=0;p<i;p++) {

		acc[i][j] = acc[i][j] + acumula(p,j)*tab[p][j];
		soma[i][j]+=tab[p][j];
	      }
	      for(int p=0;p<j;p++) {
		acc[i][j] = acc[i][j] + acumula(i,p)*tab[i][p]; 
		soma[i][j]+= tab[i][p];
	      }
	      soma[i][j] += tab[i][j];
	      acc[i][j] = acc[i][j] + acumula(i,j)*tab[i][j];
	       
	    }
	}
      int saida = 0;
      for(int k=min(r,c);k>=2;k--)
	{
	  for(int i=1;saida ==0 && i<=r;i++)
	    {
	      for(int j=1;saida ==0 && j<=c;j++)
		{
		  if(i+k>r || j+k>c)continue;
		  acumula at = acc[i+k][j+k] - acc[i-1][j+k] - acc[i+k][j-1] + acc[i-1][j-1];
		  at = at - acumula(i,j)*tab[i][j] 
		    - acumula(i+k,j+k)*tab[i+k][j+k] 
		    - acumula(i,j+k)*tab[i][j+k]
		    - acumula(i+k,j)*tab[i+k][j];
		  huge mass = soma[i+k][j+k] - soma[i-1][j+k] - soma[i+k][j-1] + soma[i-1][j-1];
		  mass =mass -(tab[i][j]+tab[i+k][j+k] + tab[i][j+k] + tab[i+k][j]); 
		  at = at*2;
		 
		  acumula tmp = acumula(i+k+i,j+k+j)*mass;
		  if(k==-233) {
		    printf("%d %d\n",i,j);
		    tmp.print();
		    at.print();
		   
		  }
		  if( at ==tmp)
		    {
		      saida  = k+1;
		      break;
		    }  
		}
	    }
	}
      printf("Case #%d: ",pp);
      if(saida<2)
	printf("IMPOSSIBLE\n");
      else 
	printf("%d\n",saida);
    }
  return 0;
}
