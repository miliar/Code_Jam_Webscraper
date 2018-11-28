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



const int nmax=111;
 

vector<vector<int> > at;
int mat[nmax][nmax];
int n;


int best(int a)
{
  // printf("oi\n");
  int ret=inf;
  //printf("%d\n",at.size());
  if(a==n)return at.size();
  for(int i=0;i<at.size();i++)
    {
      int flag=0;
      for(int j=0;j<at[i].size();j++)
	if(mat[at[i][j]][a]==1){flag=1;break;}
      if(flag==0)
	{
	  
	  at[i].push_back(a);
	  if(at.size()<ret) ret=min(ret,best(a+1));
	  at[i].resize(at[i].size()-1);
	}
    }

  vector<int> novo;
  novo.push_back(a);
  at.push_back(novo);
  if(at.size()<ret) ret=min(ret,best(a+1));
  at.resize(at.size()-1);
  return ret;

}
int main ()
{
  int tt;
  scanf("%d",&tt);
 
  int val[nmax][nmax];
  for(int pp=1;pp<=tt;pp++)
    {
      int k;
      scanf("%d %d",&n,&k);
      for(int i=0;i<n;i++)
	{
	  for(int j=0;j<k;j++)
	    {
	      scanf(" %d",&val[i][j]); 
	      //   mat[i][j]=1;
	    }
	}
      memset(mat,0,sizeof(mat));
      for(int i=0;i<n;i++)
	{
	  for(int j=0;j<n;j++)
	    {
	      for(int p=0;p<k-1;p++)
		{
		  if(val[i][p]==val[j][p])mat[i][j]=mat[j][i]=1;
		  else if(val[i][p]<val[j][p] && val[j][p+1]<val[i][p+1])mat[i][j]=mat[j][i]=1;
		}
	      if(val[i][k-1]==val[j][k-1])mat[i][j]=mat[j][i]=1;
	    }
	}

	  at.resize(0);
	  //	  printf("%d ",mat[0][1]);
      int x = best(0);
      
    
      printf("Case #%d: %d\n",pp,x);
    }
  return 0;
}
