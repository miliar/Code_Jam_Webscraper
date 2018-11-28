#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
#define lim 2001
#define pb push_back
#define mp make_pair
#define f first
#define s second

int cs,c,n,m,i,j,mn,x,y;
int C[lim];
vector <pair<int,int> > V[lim];

bool sat(int mask)
{
  int i=0,j;
  
  while(i<m)
  {
    for(j=0;j<C[i];j++)
	  if((mask & (1<<V[i][j].f))==0)
	  {
	    if(V[i][j].s==0)
		  break;
	  }
	  else
	    if(V[i][j].s==1)
		  break;
    if(j==C[i])
	  break;
    i++;
  }
  return i==m;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&n);
    scanf("%d",&m);
	for(i=0;i<m;i++)
	{
	  V[i].clear();
	  scanf("%d",&C[i]);
	  for(j=0;j<C[i];j++)
	  {
	    scanf("%d %d",&x,&y);
	    V[i].pb(mp(x-1,y));
	  }
	}
	mn=-1;
	for(i=0;i<(1<<n);i++)
	  if(sat(i))
	  {
	    if(mn==-1)
		{
		  mn=__builtin_popcount(i);
		  j=i;
		}
		if(__builtin_popcount(i)<mn)
		{
		  mn=__builtin_popcount(i);
		  j=i;
		}
	  }
	printf("Case #%d:",c+1);
	if(mn==-1)
	  printf(" IMPOSSIBLE\n");
	else
	{
	  for(i=0;i<n;i++)
	    if((j & (1<<i))==0)
		  printf(" 0");
		else
		  printf(" 1");
      printf("\n");
	}
  }
  return 0;
}
