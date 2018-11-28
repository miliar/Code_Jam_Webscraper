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

char pal[21111][25];
int mask[21111][30];
int sz[21111];

int novo[21111][2111];
int val[21111];

int grupo[21111][30];
int err[111111][30];
char chu[30];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      printf("Case #%d:",pp);
      int n,m;
      scanf("%d %d",&n,&m);
      for(int i=0;i<n;i++)
	{
	  scanf(" %s",pal[i]);
	  for(int j=0;j<26;j++)
	    {
	      int m = 0;
	      for(int p=0;pal[i][p];p++)
		m+=(pal[i][p]-'a'==j)?(1<<p):0;
	      mask[i][j]=m;
	    }
	  sz[i]=strlen(pal[i]);
	}
      for(int xx=0;xx<m;xx++)
	{
	  scanf(" %s",chu+1);
	  for(int j=0;j<n;j++)
	    {
	      err[j][0]=0;
	      grupo[j][0]=sz[j];
	    }
	  int tem = 11;

	  for(int j=1;j<=26;j++)
	    {
	      int pp = 1;
	      for(int i=0;i<n;i++)
		{
		  if(mask[i][chu[j]-'a']!=0)
		    {
		      val[grupo[i][j-1]]=1;
		    }
		  if(novo[grupo[i][j-1]][mask[i][chu[j]-'a']]==0)
		    {
		      novo[grupo[i][j-1]][mask[i][chu[j]-'a']]=pp++;
		    }
		  grupo[i][j]=novo[grupo[i][j-1]][mask[i][chu[j]-'a']];
		}
	      for(int i=0;i<n;i++)
		{
		  err[i][j]=err[i][j-1];
		  if(mask[i][chu[j]-'a']==0 && val[grupo[i][j-1]]==1)
		    err[i][j]++;
		  novo[grupo[i][j-1]][mask[i][chu[j]-'a']]=0;
		}
	      for(int i=0;i<n;i++)
		val[grupo[i][j-1]]=0;
	    }
	  int maior=-1,pos=0;
	  for(int i=0;i<n;i++)
	    {
	      if(err[i][26]>maior)
		{
		  maior=err[i][26];
		  pos=i;
		}
	    }
	  printf(" %s",pal[pos]);
	}
      printf("\n");
    }
  return 0;
}

