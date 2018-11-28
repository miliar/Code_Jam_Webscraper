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


char mapa[55][55];
int n,m,f;
huge best[55][55][55][55];
int foi[55][55][55][55];

huge dp(int a,int b,int c,int d)
{
  huge ret=inf;
  
  if(a==n-1)return 0;
  int i;
  //printf("%d %d %d %d=%d\n",a,b,c,d,foi[a][b][c][d]);
  //  if(a==3)printf("%d ",b);
  
  //if(best[a][b][c][d]==-1)
  //  {


      //if(foi[a][b][c][d])return inf;
      foi[a][b][c][d]=1;
      if(b>0 && mapa[a][b-1]=='.')//anda esq
	{ 
	  // printf("oi");
	  if(mapa[a+1][b-1]=='.')
	    {
	      // printf("oi");
	      for(i=a;i<n;i++)
		if(mapa[i][b-1]=='#')break;
	      if(i-a<=f+1)
		ret=min(ret,dp(i-1,b-1,0,m));
	    }
	  else
	    {
	      
	      // ret=min(ret,dp(a,b+1));
	      //if(ant!=1)//n veio da esquerda
		if(!foi[a][b-1][c][d])ret=min(ret,dp(a,b-1,c,d));//pra esq
	      
	      mapa[a+1][b-1]='.';
	      ret=min(ret,1+dp(a,b,b-1,d));
	   
	      mapa[a+1][b-1]='#';
	    }
	  
	}
      if(b+1<m && mapa[a][b+1]=='.')//anda dir
	{
	  // printf("%d %d ",a,b);
	  if(mapa[a+1][b+1]=='.')
	    {
	      
	      for(i=a;i<n;i++)
		if(mapa[i][b+1]=='#')break;
	      if(i-a<=f+1)
		ret=min(ret,dp(i-1,b+1,0,m));
	    }
	  else 
	    {
	      // if(ant!=2)//n veio da dir
	     	if(!foi[a][b+1][c][d])ret=min(ret,dp(a,b+1,c,d));//pra direita 

	      //printf("oi");
	      //   if(a==0 && b==3)printf("oi");
	      mapa[a+1][b+1]='.';
	      ret=min(ret,1+dp(a,b,c,b+1));
	   
	      mapa[a+1][b+1]='#';
	      //    if(a==0 && b==3)printf("endoi");
	    }
	}
      best[a][b][c][d]=ret;
      foi[a][b][c][d]=0;
      // }
  return best[a][b][c][d];
}

int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      
      scanf("%d %d %d",&n,&m,&f);
      for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	  {
	    scanf(" %c",&mapa[i][j]);
	    
	    // for(int k=0;k<3;k++)foi[i][j][k]=0;
	  }
      
      for(int i=0;i<55;i++)
	for(int j=0;j<55;j++)
	  for(int k=0;k<55;k++)
	    for(int p=0;p<55;p++)
	      {
		best[i][j][k][p]=-1;
		foi[i][j][k][p]=0;
	      }

      for(int j=0;j<55;j++)
	for(int k=0;k<55;k++)
	  for(int p=0;p<55;p++)
	    best[n-1][j][k][p]=0;

      memset(foi,0,sizeof(foi));
      
	
      
      huge x=dp(0,0,0,m);
      
      
      /*  for(int i=0;i<n;i++)
	{
	  
	  for(int j=0;j<m;j++)
	    {
	      huge x=inf;
	      for(int k=0;k<55;k++)
		for(int p=0;p<55;p++)
		  if(best[i][j][k][p]!=-1)x=min(x,best[i][j][k][p]);
	      if(x<inf)
		printf("<%lld>",x);
	      else
		printf("<.>");
	    }
	  printf("\n");
	}*/
      printf("Case #%d: ",pp);
      if(x>=inf)
	printf("No\n");
      else
	printf("Yes %lld\n",x);
    }
  return 0;
}
